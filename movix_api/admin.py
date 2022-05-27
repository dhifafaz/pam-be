from django.contrib import admin

# Register your models here.
from .models import Film
from django.utils.html import format_html

@admin.display(description="image")
class FilmData(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('title', 'rating', 'tahun_terbit', 
                'genre', 'durasi', 'description', 
                'sutradara', 'image_file')
    list_filter = ('title','rating', 'genre', 'tahun_terbit')
    # fieldsets = ('title', 'rating', 'tahun_terbit', 
    #             'genre', 'durasi', 'description', 
    #             'sutradara', 'image_file')
    # add_fieldsets = ('title', 'rating', 'tahun_terbit', 
    #             'genre', 'durasi', 'description', 
    #             'sutradara', 'image_file')
    search_fields = ('title', 'sutradara')
    # readonly_fields = ('image_file', )
    
    def image_file(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.image)

admin.site.register(Film, FilmData)