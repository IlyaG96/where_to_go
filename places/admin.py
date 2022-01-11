from django.contrib import admin
from .models import Post
from .models import Image
# Register your models here.


class PostImageAdmin(admin.StackedInline):
    model = Image


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
