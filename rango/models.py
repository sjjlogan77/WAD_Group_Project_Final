from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

slug = models.SlugField(unique=True)

class Movie(models.Model):
    title = models.CharField(max_length=128, unique=True)
    releaseDate = models.CharField(max_length=128)
    avgRating = models.FloatField(default=-1)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Movies'
    
    def __str__(self):
        return self.title
        
class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)    
    user = models.CharField(max_length=128)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    
    def __str__(self):
        return str(self.rating)

#=-------------
class Tv(models.Model):
    title = models.CharField(max_length=128, unique=True)
    releaseDate = models.CharField(max_length=128)
    avgRating = models.FloatField(default=-1)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tv, self).save(*args, **kwargs)

    
    class Meta:
        verbose_name_plural = 'Shows'
    
    def __str__(self):
        return self.title


class TvRating(models.Model):
    tv = models.ForeignKey(Tv, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    user = models.CharField(max_length=128)
    
    def __str__(self):
        return str(self.rating)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default = 16)

    def __str__(self):
        return self.user.username