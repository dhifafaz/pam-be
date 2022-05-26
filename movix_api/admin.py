from django.contrib import admin

# Register your models here.
from .models import Film

class FilmData(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('title', 'rating', 'tahun_terbit', 
                'genre', 'durasi', 'description', 
                'sutradara', 'image')

admin.site.register(Film, FilmData)