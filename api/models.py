from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie, Genre
# Create your models here.

class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genre'
        allowed_methods = ['get']


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.select_related('genre').all()
        resource_name = 'movies'
        allowed_methods = ['get']
        





