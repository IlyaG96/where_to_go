from django.db import models
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=256)
    images = models.JSONField()
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates = models.JSONField()

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.title
