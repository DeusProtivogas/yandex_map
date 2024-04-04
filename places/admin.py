from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline

from places.models import Place, Photo


class PhotoInline(SortableStackedInline):
    model = Photo
    readonly_fields = ["get_image_of_place"]
    fields = ("image", "get_image_of_place", "position")

    def get_image_of_place(self, obj):
        return format_html("<img src='{url}' width='{width}' height={height} />",
                           url=obj.image.url,
                           width=min(obj.image.width, 250),
                           height=200,
        )

@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)
