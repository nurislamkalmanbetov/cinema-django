from django import template
from movies.models import Category, Movie


register = template.Library()


@register.simple_tag()
def get_categories():
    """Display all categories"""
    return Category.objects.all()
# how to show all categories in post_list and in post_detail


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count=5):
    """Display last 5 new movies"""
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies": movies}
