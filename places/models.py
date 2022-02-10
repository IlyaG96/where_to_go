from django.db import models
from tinymce.models import HTMLField


def get_file_path(instance, filename):
    return f"{instance.point.title}/{filename}"


class Point(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок",
        help_text="Здесь заголовок",
        unique=True)
    description_short = HTMLField(
        verbose_name="Краткое описание",
        help_text="Здесь краткое описание места",
        blank=True)
    description_long = HTMLField(
        verbose_name="Полное описание",
        help_text="Здесь полное описание места",
        blank=True)
    longitude = models.FloatField(
        verbose_name="Долгота")
    latitude = models.FloatField(
        verbose_name="Широта")

    class Meta:
        verbose_name = "Точка на карте"
        verbose_name_plural = "Все точки на карте"

    def __str__(self):
        return self.title


class Image(models.Model):
    point = models.ForeignKey(
        Point,
        on_delete=models.CASCADE,
        related_name="images")
    image = models.ImageField(
        upload_to=get_file_path,
        verbose_name="Картинка")
    position = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядковый номер картинки")

    class Meta:
        ordering = ["position"]
        verbose_name = "Изображение"
        verbose_name_plural = "Все изображения"

    def __str__(self):
        return f"фотография {self.point.title}"
