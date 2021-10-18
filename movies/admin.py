from django.contrib import admin
from .models import Movie, Genre

# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year', 'stock')

admin.site.register(Movie, MovieAdmin)

