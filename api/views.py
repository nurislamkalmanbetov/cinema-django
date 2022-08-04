from django.shortcuts import render
from movies.models import Category, Actor, Movie
from .serializers import *

from rest_framework.generics import ListAPIView


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ActorListAPIView(ListAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class MovieListAPIView(ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
