from django.contrib import admin

# Register your models here.
from .models import Film
from django.utils.html import format_html

class FilmData(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('title', 'rating', 'tahun_terbit', 
                'genre', 'durasi', 'description', 
                'sutradara', 'image')
    readonly_fields = ('image', )
    
    def image(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.image)

admin.site.register(Film, FilmData)