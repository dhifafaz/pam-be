from rest_framework import serializers
from .models import (
    Film,
)
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class FilmSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Film
        fields = ('title', 'rating', 'tahun_terbit', 
                'genre', 'durasi', 'description', 
                'sutradara', 'image')
