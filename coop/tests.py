from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from .models import Application, Branch, ContactMessage, FormDoc, NewsPost, Offering, Product, Program
from .templatetags.coop_extras import richtext


class SiteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed", verbosity=0)
        User = get_user_model()
        cls.member = User.objects.create_user("member@example.com", "member@example.com", "a-strong-pass-123")
        cls.staff = User.objects.create_user("staff@example.com", "staff@example.com", "a-strong-pass-123", is_staff=True)

    def setUp(self):
        cache.clear()

    def test_public_pages_render(self):
        for name in ["home", "products", "branches", "news", "calculator", "contact", "faqs", "stories", "forms", "login", "register"]:
            with self.subTest(name=name):
                self.assertEqual(self.client.get(reverse(name)).status_code, 200)

    def test_seed_has_eleven_branches_and_is_idempotent(self):
        call_command("seed", verbosity=0)
        self.assertEqual(Branch.objects.count(), 11)

    def test_branch_province_filter(self):
        r = self.client.get(reverse("branches"), {"province": "Agusan del Norte"})
        self.assertContains(r, "Butuan")
        self.assertNotContains(r, "Tandag")

    def test_contact_saves_message(self):
        r = self.client.post(reverse("contact"), {"name": "Ana", "email": "ana@example.com", "phone": "0917 123 4567", "topic": "Membership", "message": "Hello, I want to join."})
        self.assertRedirects(r, reverse("contact"))
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_is_rate_limited(self):
        for _ in range(5):
            self.client.post(reverse("contact"), {"name": "", "email": "", "message": ""})
        r = self.client.post(reverse("contact"), {"name": "", "email": "", "message": ""})
        self.assertEqual(r.status_code, 429)

    def test_register_logs_in(self):
        r = self.client.post(reverse("register"), {"email": "New@Example.com", "password": "another-strong-pass-9"})
        self.assertRedirects(r, reverse("apply"))
        self.assertTrue(get_user_model().objects.filter(username="new@example.com").exists())

    def test_register_rejects_weak_password(self):
        r = self.client.post(reverse("register"), {"email": "x@example.com", "password": "123"})
        self.assertEqual(r.status_code, 200)
        self.assertFalse(get_user_model().objects.filter(username="x@example.com").exists())

    def test_apply_requires_login(self):
        r = self.client.get(reverse("apply"))
        self.assertEqual(r.status_code, 302)
        self.assertIn(reverse("login"), r.url)

    def test_membership_application_ignores_injected_status(self):
        self.client.force_login(self.member)
        branch = Branch.objects.first()
        self.client.post(reverse("apply"), {"full_name": "Ana Cruz", "phone": "09171234567", "branch": branch.pk,
                                            "status": "Approved", "amount": "999999"})
        a = Application.objects.get()
        self.assertEqual(a.status, Application.Status.SUBMITTED)
        self.assertEqual(a.kind, Application.Kind.MEMBERSHIP)
        self.assertIsNone(a.amount)
        self.assertEqual(a.user, self.member)

    def test_loan_application_requires_loan_fields(self):
        self.client.force_login(self.member)
        branch = Branch.objects.first()
        r = self.client.post(reverse("apply_kind", args=["Loan"]), {"full_name": "Ana", "phone": "0917", "branch": branch.pk})
        self.assertEqual(r.status_code, 200)
        self.assertFalse(Application.objects.exists())
        self.client.post(reverse("apply_kind", args=["Loan"]), {"full_name": "Ana", "phone": "0917", "branch": branch.pk,
                                                                "loan_type": "Business", "amount": "50000", "term_months": "12"})
        self.assertEqual(Application.objects.get().kind, "Loan")

    def test_members_only_see_their_own_applications(self):
        other = get_user_model().objects.create_user("o@example.com", "o@example.com", "a-strong-pass-123")
        Application.objects.create(user=other, full_name="Other Person", phone="1", branch=Branch.objects.first())
        self.client.force_login(self.member)
        self.assertNotContains(self.client.get(reverse("my_applications")), "Other Person")

    def test_dashboard_is_staff_only_and_updates_status(self):
        a = Application.objects.create(user=self.member, full_name="Ana", phone="1", branch=Branch.objects.first())
        self.client.force_login(self.member)
        self.assertEqual(self.client.get(reverse("dashboard")).status_code, 302)
        self.client.post(reverse("set_status", args=[a.pk]), {"status": "Approved"})
        a.refresh_from_db()
        self.assertEqual(a.status, "Submitted")
        self.client.force_login(self.staff)
        self.assertEqual(self.client.get(reverse("dashboard")).status_code, 200)
        self.client.post(reverse("set_status", args=[a.pk]), {"status": "Approved"})
        a.refresh_from_db()
        self.assertEqual(a.status, "Approved")

    def test_language_switch_and_open_redirect_guard(self):
        r = self.client.get(reverse("set_lang", args=["ceb"]), {"next": "https://evil.example.com/"})
        self.assertEqual(r.url, "/")
        self.assertContains(self.client.get(reverse("home")), "Mahimong Membro")

    def test_login_is_case_insensitive(self):
        r = self.client.post(reverse("login"), {"username": "Member@Example.com", "password": "a-strong-pass-123"})
        self.assertEqual(r.status_code, 302)

    def test_real_content_is_seeded(self):
        self.assertEqual(Product.objects.count(), 6)
        self.assertEqual(Program.objects.count(), 14)
        self.assertTrue(Offering.objects.filter(name="MAPS-Fisherfolks Loan").exists())
        self.assertEqual(NewsPost.objects.count(), 15)
        self.assertEqual(FormDoc.objects.count(), 7)
        call_command("seed", verbosity=0)               # running again must not duplicate anything
        self.assertEqual(Program.objects.count(), 14)
        call_command("seed", "--replace", verbosity=0)  # nor must a full reload
        self.assertEqual(NewsPost.objects.count(), 15)

    def test_every_service_and_news_page_renders(self):
        for c in Product.objects.all():
            self.assertContains(self.client.get(c.get_absolute_url()), c.category)
        for p in Program.objects.all():
            self.assertContains(self.client.get(p.get_absolute_url()), p.name)
        for n in NewsPost.objects.all():
            self.assertEqual(self.client.get(n.get_absolute_url()).status_code, 200)
        self.assertEqual(self.client.get("/services/loans/nope/").status_code, 404)

    def test_loan_program_links_to_prefilled_application(self):
        p = Program.objects.get(slug="agricultural-loans")
        self.assertContains(self.client.get(p.get_absolute_url()), "?type=Agricultural")
        self.client.force_login(self.member)
        r = self.client.get(reverse("apply_kind", args=["Loan"]), {"type": "Agricultural"})
        self.assertContains(r, 'value="Agricultural" selected')

    def test_news_tag_filter_and_paging(self):
        r = self.client.get(reverse("news"), {"tag": "Outreach"})
        self.assertContains(r, "Walang Gutom")
        self.assertNotContains(r, "Fire Safety")
        self.assertEqual(self.client.get(reverse("news"), {"page": 2}).status_code, 200)

    def test_contact_rejects_bad_phone(self):
        r = self.client.post(reverse("contact"), {"name": "Ana", "email": "ana@example.com", "phone": "call me",
                                                  "topic": "Loans", "message": "Hello there friends"})
        self.assertEqual(r.status_code, 200)
        self.assertFalse(ContactMessage.objects.exists())

    def test_richtext_escapes_and_formats(self):
        html = richtext("Intro <b>x</b>\n\n- one\n- two")
        self.assertIn("<p>Intro &lt;b&gt;x&lt;/b&gt;</p>", html)
        self.assertIn("<ul><li>one</li><li>two</li></ul>", html)

    def test_health(self):
        self.assertEqual(self.client.get(reverse("health")).json(), {"status": "ok"})
