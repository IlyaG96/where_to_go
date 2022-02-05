from django.contrib import admin
from .models import Point
from .models import Image
from django.utils.html import format_html, mark_safe
from adminsortable2.admin import SortableInlineAdminMixin


class PointImageAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    readonly_fields = "image_preview",

    def image_preview(self, image):

        response = format_html("<img src={} width=150>", mark_safe(image.image.url))

        return response


@admin.register(Point)
class Point(admin.ModelAdmin):
    search_fields = ["title"]

    inlines = [
        PointImageAdmin
    ]

    class Meta:
        model = Point


@admin.register(Image)
class Image(admin.ModelAdmin):
    raw_id_fields = ("point",)
