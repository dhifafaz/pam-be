from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import Index
from .views import (
    FilmView,
)

router  = DefaultRouter()
router.register('film-list', FilmView, basename='film-list')

urlpatterns = [
    path('', include(router.urls)),
]