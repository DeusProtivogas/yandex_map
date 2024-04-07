from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from places.views import main_page, place_detail_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    path("places/<str:place_id>/", place_detail_view),
    path("", main_page)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
