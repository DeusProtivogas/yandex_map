from django.contrib import admin
from django import forms
from django.db.models import TextField
from django.utils.safestring import mark_safe
from django.db import models
from places.models import Place, Photo
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


class PhotoInline(SortableStackedInline):
    model = Photo
    readonly_fields = ["place_image"]
    fields = ("image", "place_image", "position")

    def get_image_of_place(self, obj):
        return mark_safe("<img src='{url}' width='{width}' height={height} />".format(
            url=obj.image.url,
            width=min(obj.image.width, 250),
            height=min(obj.image.height, 200),
        )
    )

@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):\
    inlines = [
        PhotoInline,
    ]

# Register your models here.

admin.site.register(Photo)