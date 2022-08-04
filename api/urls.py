from django.urls import path

from .views import *


urlpatterns = [
    path("category_list/", CategoryListAPIView.as_view()),
    path("actor_list/", ActorListAPIView.as_view()),
    path("movie_list/", MovieListAPIView.as_view()),
]
