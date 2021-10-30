from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    release_date = models.IntegerField() #Store UNIX time
    poster_url = models.URLField()
    synopsis = models.TextField()

    def __str__(self):
        return self.movie_title