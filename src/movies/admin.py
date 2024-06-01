from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'idx', 'rating_avg', 'rating_count']
    readonly_fields = ['idx', 'rating_avg', 'rating_count']
    search_fields = ['id']

admin.site.register(Movie, MovieAdmin)  
