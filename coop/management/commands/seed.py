"""Load SOEMCO content from coop/content.py.

    python manage.py seed            # add anything missing, update existing items by name
    python manage.py seed --replace  # delete and reload services, news, stories, FAQs, forms
                                     # (branches, applications, messages and accounts are kept)
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify

from coop import content as C
from coop.models import (Announcement, Branch, Faq, FormDoc, NewsPost, Offering, Product, Program,
                         Testimonial)


def summarize(text, limit=220):
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(",;:—-")
    return cut + "…"


class Command(BaseCommand):
    help = "Load SOEMCO starter content (safe to run more than once)."

    def add_arguments(self, parser):
        parser.add_argument("--replace", action="store_true",
                            help="Delete and reload services, news, stories, FAQs, forms and announcements")

    @transaction.atomic
    def handle(self, *args, replace=False, **opts):
        if replace:
            for model in (Product, NewsPost, Testimonial, Faq, FormDoc, Announcement):
                model.objects.all().delete()  # programs, offerings and galleries are deleted with their parents
            self.stdout.write("Cleared old content.")
        NewsPost.objects.filter(title__in=C.OLD_PLACEHOLDER_NEWS).delete()

        for name, province, address, head, map_url, is_main, _photo in C.BRANCHES:
            Branch.objects.update_or_create(name=name, defaults=dict(
                province=province, address=address, head=head, map_url=map_url, is_main=is_main))

        for n, cat in enumerate(C.SERVICES, 1):
            product = (Product.objects.filter(slug=cat["slug"]).first()
                       or Product.objects.filter(category=cat["name"]).first() or Product())
            product.category, product.slug, product.icon = cat["name"], cat["slug"], cat["icon"]
            product.summary, product.sort_order = cat["summary"], n
            product.highlights = product.highlights or ""
            product.save()
            for pn, prog in enumerate(cat["programs"], 1):
                program, _ = Program.objects.update_or_create(category=product, slug=prog["slug"], defaults=dict(
                    name=prog["name"], summary=prog["summary"], people=prog.get("people", ""),
                    loan_type=prog.get("loan_type", ""), sort_order=pn))
                for on, (oname, desc, elig, _img) in enumerate(prog["offerings"], 1):
                    Offering.objects.update_or_create(program=program, name=oname, defaults=dict(
                        description=desc, eligibility=elig, sort_order=on))

        for post in C.NEWS:
            body = "\n\n".join(post["body"])
            NewsPost.objects.update_or_create(slug=post["slug"], defaults=dict(
                title=post["title"], published_on=post["date"], tag=post["tag"], body=body,
                summary=summarize(post["body"][0]), is_published=True))

        for title, name, info, branch, _photo, story in C.STORIES:
            Testimonial.objects.update_or_create(name=name, defaults=dict(title=title, info=info, branch=branch, story=story))

        for n, (q, a) in enumerate(C.FAQS, 1):
            Faq.objects.update_or_create(question=q, defaults=dict(answer=a, sort_order=n))

        for n, (title, category, desc, path) in enumerate(C.FORMS, 1):
            doc, created = FormDoc.objects.get_or_create(title=title, defaults=dict(link=C.UPLOADS + path))
            doc.category, doc.description, doc.sort_order = category, desc, n
            if not doc.file:
                doc.link = C.UPLOADS + path
            doc.save()
        FormDoc.objects.filter(title="Official SOEMCO forms").delete()  # placeholder from the first version

        for title, body, active in C.ANNOUNCEMENTS:
            Announcement.objects.get_or_create(title=title, defaults=dict(body=body, is_active=active))

        self.stdout.write(self.style.SUCCESS(
            f"SOEMCO content loaded: {Branch.objects.count()} branches, {Product.objects.count()} service categories, "
            f"{Program.objects.count()} programs, {Offering.objects.count()} products, {NewsPost.objects.count()} news posts, "
            f"{Testimonial.objects.count()} stories, {Faq.objects.count()} FAQs, {FormDoc.objects.count()} forms."))
        self.stdout.write("Next: python manage.py import_photos   (downloads photos and form files)")
