"""Copy SOEMCO's photos, logo and downloadable forms from soemco.org.ph into this site.

    python manage.py import_photos            # fill in whatever is missing
    python manage.py import_photos --force    # re-download and replace everything

Photos are resized to at most 1600 px wide and saved as JPEG so pages load fast.
Run `python manage.py seed` first so the records exist.
"""
import io
import os
import urllib.request

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand
from PIL import Image, ImageOps

from coop import content as C
from coop.models import (Branch, FormDoc, HeroSlide, NewsImage, NewsPost, Offering, Product, Program,
                         Testimonial)


def fetch(path):
    req = urllib.request.Request(C.UPLOADS + path, headers={"User-Agent": "Mozilla/5.0 (SOEMCO website importer)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def to_web_jpeg(data, max_width=1600):
    im = ImageOps.exif_transpose(Image.open(io.BytesIO(data)))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    elif im.mode != "RGB":
        im = im.convert("RGB")
    im.thumbnail((max_width, max_width * 3))
    out = io.BytesIO()
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    return out.getvalue()


class Command(BaseCommand):
    help = "Download SOEMCO photos, logo and forms from soemco.org.ph into this site's media folder."

    def add_arguments(self, parser):
        parser.add_argument("--force", action="store_true", help="Replace photos and files that are already set")

    def handle(self, *args, force=False, **opts):
        self.force, self.ok, self.failed, self.cache = force, 0, 0, {}

        # Logo (original PNG, transparent background)
        if force or not default_storage.exists("brand/logo.png"):
            data = self._get(C.LOGO)
            if data:
                if default_storage.exists("brand/logo.png"):
                    default_storage.delete("brand/logo.png")
                default_storage.save("brand/logo.png", ContentFile(data))
                self._done("Logo")

        # Home-page banner
        if force or not HeroSlide.objects.exists():
            for s in HeroSlide.objects.all():
                s.image.delete(save=False)
                s.delete()
            for n, (path, caption) in enumerate(C.HERO, 1):
                jpg = self._jpeg(path)
                if jpg:
                    slide = HeroSlide(caption=caption, sort_order=n)
                    slide.image.save(f"hero-{n}.jpg", ContentFile(jpg), save=True)
                    self._done(f"Banner: {caption}")

        # Services
        for cat in C.SERVICES:
            product = Product.objects.filter(slug=cat["slug"]).first()
            self._set(product, "image", cat["image"], f"Service: {cat['name']}")
            for prog in cat["programs"]:
                program = Program.objects.filter(category=product, slug=prog["slug"]).first() if product else None
                self._set(program, "image", prog.get("image"), f"Program: {prog['name']}")
                self._set(program, "photo2", prog.get("photo2"), f"Program team photo: {prog['name']}")
                for oname, _d, _e, img in prog["offerings"]:
                    off = Offering.objects.filter(program=program, name=oname).first() if program else None
                    self._set(off, "image", img, f"Product: {oname}")

        # Branches and stories
        for name, *_rest, photo in C.BRANCHES:
            self._set(Branch.objects.filter(name=name).first(), "photo", photo, f"Branch: {name}")
        for _t, name, _i, _b, photo, _s in C.STORIES:
            self._set(Testimonial.objects.filter(name=name).first(), "photo", photo, f"Story: {name}")

        # News: first image is the cover, the rest go in the gallery
        for post in C.NEWS:
            obj = NewsPost.objects.filter(slug=post["slug"]).first()
            imgs = post["images"]
            self._set(obj, "image", imgs[0] if imgs else None, f"News: {post['title'][:50]}")
            if obj and len(imgs) > 1 and (force or not obj.gallery.exists()):
                for g in obj.gallery.all():
                    g.image.delete(save=False)
                    g.delete()
                for n, path in enumerate(imgs[1:], 1):
                    jpg = self._jpeg(path)
                    if jpg:
                        g = NewsImage(post=obj, sort_order=n)
                        g.image.save(f"news-{obj.pk}-{n}.jpg", ContentFile(jpg), save=True)
                        self._done(f"  gallery photo {n}")

        # Downloadable forms: keep the original Word/PDF file
        for title, _cat, _desc, path in C.FORMS:
            doc = FormDoc.objects.filter(title=title).first()
            if doc and (force or not doc.file):
                data = self._get(path)
                if data:
                    if doc.file:
                        doc.file.delete(save=False)
                    doc.file.save(os.path.basename(path), ContentFile(data), save=True)
                    self._done(f"Form: {title}")

        style = self.style.SUCCESS if not self.failed else self.style.WARNING
        self.stdout.write(style(f"Done: {self.ok} files saved, {self.failed} failed."))

    # ---- helpers
    def _set(self, obj, field, path, label):
        if not path:
            return
        if obj is None:
            self.stdout.write(f"  skip  {label} (not in database, run `python manage.py seed` first)")
            return
        current = getattr(obj, field)
        if current and not self.force:
            return
        jpg = self._jpeg(path)
        if jpg:
            if current:
                current.delete(save=False)
            current.save(f"{obj._meta.model_name}-{obj.pk}-{field}.jpg", ContentFile(jpg), save=True)
            self._done(label)

    def _jpeg(self, path):
        if path not in self.cache:
            data = self._get(path)
            try:
                self.cache[path] = to_web_jpeg(data) if data else None
            except Exception as e:  # not a readable image
                self.failed += 1
                self.stderr.write(f"  fail  {path}: {e}")
                self.cache[path] = None
        return self.cache[path]

    def _get(self, path):
        try:
            return fetch(path)
        except Exception as e:  # network error, 404, etc.
            self.failed += 1
            self.stderr.write(f"  fail  {path}: {e}")
            return None

    def _done(self, label):
        self.ok += 1
        self.stdout.write(f"  saved {label}")
