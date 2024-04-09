from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline

from places.models import Place, Photo


class PhotoInline(SortableStackedInline):
    model = Photo
    readonly_fields = ["get_preview"]
    fields = ("image", "get_preview", "position")

    def get_preview(self, obj):
        return format_html(
            "<img src='{url}' style='max-width:{max_width}px; max-height:{max_height}px'/>",
            url=obj.image.url,
            max_width=min(obj.image.width, 250),
            max_height=200,
                           )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)
