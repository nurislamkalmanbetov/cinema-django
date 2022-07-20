from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    """Review Inline"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Movie"""
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft", )
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"), )
        }),
        (None, {
            "fields": (("description", "poster"), )
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"), )
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"), )
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fess_in_world"), )
        }),
        ("Options", {
            "fields": (("url", "draft"), )
        }),
    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Reviews"""
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genres"""
    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Actors"""
    list_display = ("name", "age")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "movie", "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """MovieShots"""
    list_display = ("title", "movie")

# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Genre)
# admin.site.register(Movie)
# admin.site.register(MovieShots)
# admin.site.register(Actor)
# admin.site.register(Rating)
# admin.site.register(RatingStar)
# admin.site.register(Reviews)
