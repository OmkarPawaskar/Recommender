import datetime
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone

from ratings.models import Rating
# Create your models here.

RATING_CALC_TIME = 1

class Movie(models.Model):

    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField()
    release_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    ratings = GenericRelation(Rating) #queryset
    rating_last_updated = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    rating_count = models.IntegerField(null=True, blank=True)
    rating_avg = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True) #5.00, 0d.00

    def rating_avg_display(self):
        now = timezone.now()
        if not self.rating_last_updated:
            return self.calculate_rating()
        if self.rating_last_updated > now - datetime.timedelta(minutes=RATING_CALC_TIME):
            return self.rating_avg
        return self.calculate_rating()

    def calculate_ratings_count(self):
        return self.ratings.all().count()

    def calculate_ratings_avg(self):
        return self.ratings.all().avg()

    def calculate_rating(self, save=True):
        rating_avg = self.calculate_ratings_avg()
        rating_count = self.calculate_ratings_count()
        self.rating_avg = rating_avg
        self.rating_count = rating_count
        self.rating_last_updated = timezone.now()
        if save:
            self.save()
        return self.rating_avg

    def __str__(self):
        return self.title