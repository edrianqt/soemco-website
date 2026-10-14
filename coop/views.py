from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import connection
from django.db.models import Count, Prefetch
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import ApplicationForm, ContactForm, RegisterForm
from .models import (Announcement, Application, Branch, ContactMessage, Faq, FormDoc, HeroSlide, NewsPost,
                     Product, Program, Testimonial)
from .notify import notify_staff
from .ratelimit import ratelimit


def _categories():
    return Product.objects.prefetch_related(Prefetch("programs", queryset=Program.objects.order_by("sort_order")))


def home(request):
    return render(request, "coop/home.html", {
        "products": Product.objects.all(),
        "slides": HeroSlide.objects.filter(is_active=True),
        "news": NewsPost.objects.filter(is_published=True)[:3],
        "announcements": Announcement.objects.filter(is_active=True)[:2],
        "story": Testimonial.objects.exclude(photo="").first() or Testimonial.objects.first(),
    })


# ---------------------------------------------------------------- Services
def products(request):
    return render(request, "coop/products.html", {"categories": _categories()})


def service_category(request, slug):
    category = get_object_or_404(Product, slug=slug)
    related = None
    if not category.programs.exists() and slug == "children-and-youth-laboratory-coop":
        related = Program.objects.filter(slug="aflatoun-aflateen-savings").first()
    return render(request, "coop/service_category.html", {
        "category": category, "programs": category.programs.all(), "related": related,
        "categories": Product.objects.all(),
    })


def service_program(request, category_slug, slug):
    program = get_object_or_404(Program.objects.select_related("category"), category__slug=category_slug, slug=slug)
    return render(request, "coop/service_program.html", {
        "program": program, "category": program.category,
        "offerings": program.offerings.all(),
        "siblings": program.category.programs.exclude(pk=program.pk),
    })


# ---------------------------------------------------------------- News
def news(request):
    posts = NewsPost.objects.filter(is_published=True)
    tag = request.GET.get("tag") or None
    if tag:
        posts = posts.filter(tag=tag)
    tags = (NewsPost.objects.filter(is_published=True).exclude(tag="").order_by("tag")
            .values_list("tag", flat=True).distinct())
    page = Paginator(posts, 9).get_page(request.GET.get("page"))
    return render(request, "coop/news.html", {"page": page, "posts": page.object_list, "tags": tags, "tag": tag})


def news_detail(request, slug):
    post = get_object_or_404(NewsPost, slug=slug, is_published=True)
    more = NewsPost.objects.filter(is_published=True).exclude(pk=post.pk)[:3]
    return render(request, "coop/news_detail.html", {"post": post, "gallery": post.gallery.all(), "more": more})


# ---------------------------------------------------------------- Other pages
def branches(request):
    province = request.GET.get("province") or None
    qs = Branch.objects.all()
    if province:
        qs = qs.filter(province=province)
    provinces = Branch.objects.order_by("province").values_list("province", flat=True).distinct()
    return render(request, "coop/branches.html", {"branches": qs, "provinces": provinces, "selected": province})


def calculator(request):
    return render(request, "coop/calculator.html")


def faqs(request):
    return render(request, "coop/faqs.html", {"faqs": Faq.objects.all()})


def stories(request):
    return render(request, "coop/stories.html", {"stories": Testimonial.objects.all()})


def forms_page(request):
    docs = FormDoc.objects.all()
    groups = {}
    for d in docs:
        groups.setdefault(d.category or "General", []).append(d)
    return render(request, "coop/forms.html", {"groups": groups.items(), "count": len(docs)})


@ratelimit()
def contact(request):
    form = ContactForm(request.POST or None, initial={"topic": request.GET.get("topic", "General inquiry")})
    if request.method == "POST" and form.is_valid():
        msg = form.save()
        notify_staff(f"New message: {msg.topic} from {msg.name}",
                     f"From: {msg.name} <{msg.email}>\nPhone: {msg.phone or '-'}\nTopic: {msg.topic}\n"
                     f"Branch: {msg.branch or '-'}\n\n{msg.message}\n\nManage messages: /admin/coop/contactmessage/")
        messages.success(request, "Salamat! Your message was received. Our team will get back to you within office hours.")
        return redirect("contact")
    return render(request, "coop/contact.html", {"form": form, "branches": Branch.objects.all()})


def set_lang(request, code):
    nxt = request.GET.get("next", "/")
    if not url_has_allowed_host_and_scheme(nxt, {request.get_host()}, request.is_secure()):
        nxt = "/"
    resp = redirect(nxt)
    if code in ("en", "ceb"):
        resp.set_cookie("lang", code, max_age=365 * 24 * 3600, httponly=True, samesite="Lax")
    return resp


# ---------------------------------------------------------------- Accounts & applications
@ratelimit()
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"]
        user = get_user_model().objects.create_user(username=email, email=email,
                                                    password=form.cleaned_data["password"])
        login(request, user)
        return redirect("apply")
    return render(request, "registration/register.html", {"form": form})


@login_required
def apply(request, kind="Membership"):
    kind = Application.Kind.LOAN if kind == "Loan" else Application.Kind.MEMBERSHIP
    initial = {}
    if request.GET.get("type") in Application.LoanType.values:
        initial["loan_type"] = request.GET["type"]
    form = ApplicationForm(request.POST or None, kind=kind, initial=initial)
    if request.method == "POST" and form.is_valid():
        app = form.save(commit=False)
        app.user, app.kind, app.status = request.user, kind, Application.Status.SUBMITTED
        app.save()
        notify_staff(f"New {app.kind.lower()} application: {app.full_name}",
                     f"Name: {app.full_name}\nMobile: {app.phone}\nBranch: {app.branch}\nType: {app.kind} {app.loan_type}\n"
                     f"Amount: {app.amount or '-'}\nTerm: {app.term_months or '-'} months\n\n{app.purpose}\n\n"
                     f"Review it at /dashboard/")
        messages.success(request, "Application submitted. A SOEMCO officer will contact you.")
        return redirect("my_applications")
    return render(request, "coop/apply.html", {"form": form, "kind": kind})


@login_required
def my_applications(request):
    apps = request.user.applications.select_related("branch")
    return render(request, "coop/my_applications.html", {"apps": apps})


@staff_member_required
def dashboard(request):
    kind = request.GET.get("kind")
    qs = Application.objects.select_related("branch")
    if kind in Application.Kind.values:
        qs = qs.filter(kind=kind)
    counts = dict(Application.objects.order_by().values_list("status").annotate(n=Count("id")))
    return render(request, "coop/dashboard.html", {
        "apps": qs[:100],
        "kind": kind,
        "stats": [(label, counts.get(value, 0)) for value, label in Application.Status.choices],
        "statuses": Application.Status.choices,
        "contact_messages": ContactMessage.objects.select_related("branch")[:10],
        "unhandled": ContactMessage.objects.filter(handled=False).count(),
    })


@staff_member_required
@require_POST
def set_status(request, pk):
    app = get_object_or_404(Application, pk=pk)
    status = request.POST.get("status")
    if status in Application.Status.values:
        app.status = status
        app.save(update_fields=["status", "updated"])
    return redirect("dashboard")


def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status": "ok"})
    except Exception:
        return JsonResponse({"status": "db_unavailable"}, status=503)
