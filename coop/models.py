from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Branch(models.Model):
    name = models.CharField(max_length=80)
    province = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    head = models.CharField("Branch head", max_length=80, blank=True)
    map_url = models.URLField(blank=True)
    is_main = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="branches/", blank=True)

    class Meta:
        ordering = ["-is_main", "name"]
        verbose_name_plural = "branches"

    def __str__(self):
        return self.name


class Product(models.Model):
    """A service category, e.g. Loans or Savings Deposit."""
    category = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, blank=True, help_text="Used in the page address, e.g. loans")
    summary = models.TextField()
    icon = models.CharField(max_length=8, blank=True)
    highlights = models.TextField(blank=True, help_text="One highlight per line (shown when the category has no programs)")
    sort_order = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True)

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "service category"
        verbose_name_plural = "service categories"

    def get_absolute_url(self):
        return reverse("service_category", args=[self.slug]) if self.slug else reverse("products")

    def highlight_list(self):
        return [h.strip() for h in self.highlights.splitlines() if h.strip()]

    def __str__(self):
        return self.category


class NewsPost(models.Model):
    title = models.CharField(max_length=160)
    summary = models.TextField()
    tag = models.CharField(max_length=40, blank=True)
    published_on = models.DateField()
    is_published = models.BooleanField(default=True)
    image = models.ImageField("Cover photo", upload_to="news/", blank=True)
    slug = models.SlugField(max_length=120, blank=True, help_text="Used in the page address")
    body = models.TextField(blank=True, help_text="Full article. Leave a blank line between paragraphs.")

    class Meta:
        ordering = ["-published_on", "-id"]
        verbose_name = "news post"

    def get_absolute_url(self):
        return reverse("news_detail", args=[self.slug]) if self.slug else reverse("news")

    def paragraphs(self):
        return [p.strip() for p in self.body.split("\n\n") if p.strip()]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=120)
    phone = models.CharField("Mobile number", max_length=30, blank=True)
    topic = models.CharField(max_length=30, default="General inquiry", choices=[(t, t) for t in (
        "General inquiry", "Membership", "Loans", "Savings", "Insurance", "Allied services", "Feedback")])
    branch = models.ForeignKey("Branch", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Nearest branch")
    message = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} ({self.created:%b %d})"


class Application(models.Model):
    class Kind(models.TextChoices):
        MEMBERSHIP = "Membership"
        LOAN = "Loan"

    class Status(models.TextChoices):
        SUBMITTED = "Submitted"
        UNDER_REVIEW = "UnderReview", "Under review"
        APPROVED = "Approved"
        DECLINED = "Declined"

    class LoanType(models.TextChoices):
        AGRICULTURAL = "Agricultural"
        BUSINESS = "Business"
        PERSONAL = "Personal"
        SPECIAL = "Special"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")
    kind = models.CharField(max_length=12, choices=Kind.choices, default=Kind.MEMBERSHIP)
    full_name = models.CharField(max_length=80)
    phone = models.CharField("Mobile number", max_length=30)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, verbose_name="Preferred branch")
    loan_type = models.CharField(max_length=20, choices=LoanType.choices, blank=True)
    amount = models.DecimalField("Amount (₱)", max_digits=12, decimal_places=2, null=True, blank=True,
                                 validators=[MinValueValidator(1000), MaxValueValidator(5_000_000)])
    term_months = models.PositiveIntegerField("Term (months)", null=True, blank=True,
                                              validators=[MinValueValidator(1), MaxValueValidator(120)])
    purpose = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.SUBMITTED)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.kind} – {self.full_name}"


class Testimonial(models.Model):
    title = models.CharField(max_length=80, blank=True, help_text="e.g. Sonia’s Story")
    name = models.CharField(max_length=80)
    info = models.CharField(max_length=160, blank=True, help_text="Hometown, award or membership details")
    branch = models.CharField(max_length=80, blank=True)
    story = models.TextField()
    photo = models.ImageField(upload_to="stories/", blank=True)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "FAQ"

    def __str__(self):
        return self.question


class FormDoc(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=40, default="General", help_text="e.g. Membership, Loan documents")
    sort_order = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=300, blank=True)
    file = models.FileField(upload_to="forms/", blank=True, help_text="Upload a PDF, or use the link below")
    link = models.URLField(blank=True)

    class Meta:
        ordering = ["sort_order", "title"]
        verbose_name = "downloadable form"

    def url(self):
        return self.file.url if self.file else self.link

    def file_type(self):
        name = (self.file.name if self.file else self.link).lower()
        for ext, label in ((".pdf", "PDF"), (".docx", "Word"), (".doc", "Word"), (".xlsx", "Excel")):
            if name.endswith(ext):
                return label
        return "Link"

    def __str__(self):
        return self.title


class HeroSlide(models.Model):
    """Rotating photos behind the home-page banner."""
    image = models.ImageField(upload_to="hero/")
    caption = models.CharField(max_length=120, blank=True, help_text="Shown to screen readers only")
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order"]

    def __str__(self):
        return self.caption or f"Slide {self.pk}"


class Program(models.Model):
    """A program under a service category, e.g. Agricultural Loans under Loans."""
    category = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="programs")
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    summary = models.TextField()
    image = models.ImageField(upload_to="services/", blank=True)
    photo2 = models.ImageField("Team / extra photo", upload_to="services/", blank=True)
    people = models.CharField("Contact people", max_length=160, blank=True, help_text="e.g. Supervisor: Diana B. Dano")
    loan_type = models.CharField(max_length=20, blank=True, choices=[("", "—")] + list(Application.LoanType.choices),
                                 help_text="For loan programs: pre-selects this type on the online application")
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category__sort_order", "sort_order"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("service_program", args=[self.category.slug, self.slug])


class Offering(models.Model):
    """A specific product inside a program, e.g. MAPS-Fisherfolks Loan."""
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="offerings")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, help_text="Blank line = new paragraph; lines starting with '- ' become a list")
    eligibility = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="services/", blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]

    def __str__(self):
        return self.name


class NewsImage(models.Model):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="news/")
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "gallery photo"


class Announcement(models.Model):
    """Advisory shown at the top of the home page while active."""
    title = models.CharField(max_length=160)
    body = models.TextField()
    is_active = models.BooleanField("Show on home page", default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def paragraphs(self):
        return [p.strip() for p in self.body.split("\n\n") if p.strip()]
