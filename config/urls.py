from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "SOEMCO Administration"
admin.site.site_title = "SOEMCO Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("coop.urls")),
]

# Serve uploaded forms in development; in production let the web server serve MEDIA_ROOT.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
