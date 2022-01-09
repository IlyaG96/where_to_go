from django.db import models
# Create your models here.
from where_to_go import settings


class Post(models.Model):
    title = models.CharField(max_length=256)
    description_short = models.TextField()
    description_long = models.TextField()
    longitude = models.FloatField(verbose_name="Широта")
    latitude = models.FloatField(verbose_name="Долгота")

    class Meta:
        ordering = ['title']
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self):
        return f"{self.position}, {self.post.title}"


