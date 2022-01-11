from django.db import models
# Create your models here.
from where_to_go import settings


class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name="Заголовок",
                             default="Здесь заголовок")
    description_short = models.TextField(verbose_name="Краткое описание",
                                         default="Здесь краткое описание места")
    description_long = models.TextField(verbose_name="Полное описание",
                                        default="Здесь полное описание места")
    longitude = models.FloatField(verbose_name="Широта")
    latitude = models.FloatField(verbose_name="Долгота")

    class Meta:
        ordering = ['title']
        verbose_name = 'Место'
        verbose_name_plural = 'Все места'

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, default=None,
                             on_delete=models.CASCADE,
                             related_name="image")
    image = models.ImageField(upload_to='media/',
                              verbose_name="Картинка")
    position = models.PositiveIntegerField(default=0,
                                           verbose_name="Порядковый номер картинки")

    class Meta:
        ordering = ['position']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Все изображения'

    def __str__(self):
        return f"{self.position}, {self.post.title}"


