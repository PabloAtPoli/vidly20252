from django.contrib import admin
from .models import Movie, Genre

admin.site.site_header = "Vidly Administration"
admin.site.index_title = "My Vidly Administration"

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year', 'rental_unit_price', 'units_in_inventory', 'date_created')
    search_fields = ('title', 'genre__name')
    list_filter = ('genre', 'release_year')
    ordering = ('-date_created',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)



