from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    poster_url = models.URLField()
    synopsis = models.TextField()
    cast = models.TextField()
