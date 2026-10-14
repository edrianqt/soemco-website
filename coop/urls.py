from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import EmailLoginForm
from .ratelimit import ratelimit

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.products, name="products"),
    path("services/<slug:slug>/", views.service_category, name="service_category"),
    path("services/<slug:category_slug>/<slug:slug>/", views.service_program, name="service_program"),
    path("branches/", views.branches, name="branches"),
    path("news/", views.news, name="news"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    path("calculator/", views.calculator, name="calculator"),
    path("contact/", views.contact, name="contact"),
    path("faqs/", views.faqs, name="faqs"),
    path("stories/", views.stories, name="stories"),
    path("forms/", views.forms_page, name="forms"),
    path("lang/<str:code>/", views.set_lang, name="set_lang"),
    path("account/register/", views.register, name="register"),
    path("account/login/", ratelimit()(auth_views.LoginView.as_view(authentication_form=EmailLoginForm)), name="login"),
    path("account/logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("apply/", views.apply, name="apply"),
    path("apply/<str:kind>/", views.apply, name="apply_kind"),
    path("my-applications/", views.my_applications, name="my_applications"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/application/<int:pk>/status/", views.set_status, name="set_status"),
    path("health/", views.health, name="health"),
]
