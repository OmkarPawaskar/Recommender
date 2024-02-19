from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'rating_count',  'rating_avg', 'rating_last_updated']
    readonly_fields = ['rating_avg', 'rating_count', 'rating_avg_display']


admin.site.register(Movie, MovieAdmin)  
