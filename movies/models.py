from django.db import models

# Create your models here.

class Genre(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    images_url = models.CharField(max_length=2083)
    description = models.TextField(max_length=1000, blank=True)
    duration = models.CharField(max_length=10)