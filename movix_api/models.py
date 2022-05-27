from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Film(models.Model):
    title = models.CharField(max_length=300)
    rating = models.CharField(max_length=4)
    tahun_terbit = models.CharField(max_length=4)
    genre = models.CharField(max_length=100)
    durasi = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    sutradara = models.CharField(max_length=150)
    # image = models.ImageField(upload_to='poster_film/')
    image = models.URLField(max_length=300, blank=True)
    def __str__(self):
        return  self.title
    