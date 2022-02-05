from django.contrib import admin
from .models import Point
from .models import Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin


class PostImageAdmin(SortableInlineAdminMixin, admin.StackedInline):

    model = Image
    readonly_fields = "image_preview",

    def image_preview(self, image):
        return format_html(f"<img src='{image.image.url}' width='150'")


@admin.register(Point)
class AuthorAdmin(admin.ModelAdmin):

    search_fields = ['title']

    inlines = [
        PostImageAdmin
    ]

    class Meta:
        model = Point


@admin.register(Image)
class MyModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('point',)
