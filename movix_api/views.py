from unittest import result
from collections import OrderedDict
from django.db.models import Count, Q

from .models import (
    Film,
)
from .serializers import (
    FilmSerializer,
)
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import APIView
from knox.models import AuthToken
# import pyrebase
import os

class FilmView(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    serializer_class = FilmSerializer
    queryset = Film.objects.all().order_by('-tahun_terbit')
    
    def get_queryset(self):
        # Ini Linknya http://127.0.0.1:8000/movix_api/film-list/req_ranking=1   
        req_ranking = self.request.query_params.get('req-ranking')
        if req_ranking == 1:
            queryset = Film.objects.all().order_by('-rating')
        else:
            queryset = Film.objects.all().order_by('-tahun_terbit')
        return queryset
