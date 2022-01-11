from django.contrib import admin
from .models import Post
from .models import Image
# Register your models here.
from django.utils.html import format_html


class PostImageAdmin(admin.TabularInline):

    model = Image
    readonly_fields = "image_preview",

    def image_preview(self, image):
        return format_html(f'<img src="{image.image.url}" width="200"')


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):

    inlines = [
        PostImageAdmin
    ]

    class Meta:
        model = Post


@admin.register(Image)
class PostImageAdmin(admin.ModelAdmin):
    pass

