from django.contrib import admin
from django.utils.html import format_html

from .models import (Announcement, Application, Branch, ContactMessage, Faq, FormDoc, HeroSlide, NewsImage,
                     NewsPost, Offering, Product, Program, Testimonial)


def _thumb(f):
    if not f:
        return "–"
    return format_html('<img src="{}" style="height:44px;width:66px;object-fit:cover;border-radius:6px">', f.url)


class ThumbMixin:
    @admin.display(description="Photo")
    def thumb(self, obj):
        return _thumb(getattr(obj, "photo", None) or getattr(obj, "image", None))


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created")
    list_editable = ("is_active",)


@admin.register(HeroSlide)
class HeroSlideAdmin(ThumbMixin, admin.ModelAdmin):
    list_display = ("thumb", "caption", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")


@admin.register(Branch)
class BranchAdmin(ThumbMixin, admin.ModelAdmin):
    list_display = ("thumb", "name", "province", "head", "is_main")
    list_display_links = ("thumb", "name")
    list_filter = ("province",)
    search_fields = ("name", "address", "head")


class ProgramInline(admin.TabularInline):
    model = Program
    fields = ("name", "slug", "sort_order")
    prepopulated_fields = {"slug": ("name",)}
    show_change_link = True
    extra = 0


@admin.register(Product)
class ProductAdmin(ThumbMixin, admin.ModelAdmin):
    list_display = ("thumb", "category", "slug", "sort_order")
    list_display_links = ("thumb", "category")
    list_editable = ("sort_order",)
    prepopulated_fields = {"slug": ("category",)}
    inlines = [ProgramInline]


class OfferingInline(admin.StackedInline):
    model = Offering
    fields = (("name", "sort_order"), "description", "eligibility", "image")
    extra = 0


@admin.register(Program)
class ProgramAdmin(ThumbMixin, admin.ModelAdmin):
    list_display = ("thumb", "name", "category", "loan_type", "sort_order")
    list_display_links = ("thumb", "name")
    list_filter = ("category",)
    list_editable = ("sort_order",)
    search_fields = ("name", "summary", "offerings__name")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [OfferingInline]


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


@admin.register(NewsPost)
class NewsAdmin(ThumbMixin, admin.ModelAdmin):
    list_display = ("thumb", "title", "tag", "published_on", "is_published")
    list_display_links = ("thumb", "title")
    list_filter = ("is_published", "tag")
    list_editable = ("is_published",)
    search_fields = ("title", "summary", "body")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_on"
    inlines = [NewsImageInline]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "kind", "loan_type", "amount", "branch", "status", "created")
    list_filter = ("status", "kind", "branch")
    list_editable = ("status",)
    search_fields = ("full_name", "phone", "user__email")
    readonly_fields = ("user", "created", "updated")


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "topic", "branch", "email", "phone", "created", "handled")
    list_filter = ("handled", "topic", "branch")
    list_editable = ("handled",)
    search_fields = ("name", "email", "phone", "message")
    readonly_fields = ("name", "email", "phone", "topic", "branch", "message", "created")


@admin.register(Testimonial)
class TestimonialAdmin(ThumbMixin, admin.ModelAdmin):
    list_display = ("thumb", "name", "branch")
    list_display_links = ("thumb", "name")


@admin.register(FormDoc)
class FormDocAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "file_type", "sort_order")
    list_filter = ("category",)
    list_editable = ("sort_order",)


admin.site.register(Faq, list_display=("question", "sort_order"), list_editable=("sort_order",))
