from django.db import models
from tinymce.models import HTMLField


def get_file_path(instance, filename):
    return f"media/{instance.post.title}/{filename}"


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок",
        default="Здесь заголовок",
        unique=True)
    description_short = HTMLField(
        verbose_name="Краткое описание",
        default="Здесь краткое описание места")
    description_long = HTMLField(
        verbose_name="Полное описание",
        default="Здесь полное описание места")
    longitude = models.FloatField(
        verbose_name="Широта")
    latitude = models.FloatField(
        verbose_name="Долгота")

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Все места"

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(
        Post,
        default=None,
        null=True,
        on_delete=models.CASCADE,
        related_name="images")
    image = models.ImageField(
        upload_to=get_file_path,
        verbose_name="Картинка")
    position = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядковый номер картинки")

    class Meta:
        ordering = ["position"]
        verbose_name = "Изображение"
        verbose_name_plural = "Все изображения"

    def __str__(self):
        return f"{self.position}, {self.post.title}"
