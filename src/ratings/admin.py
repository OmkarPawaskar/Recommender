from django.contrib import admin
from .models import Rating

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    readonly_fields = ['content_object']


admin.site.register(Rating, RatingAdmin)
