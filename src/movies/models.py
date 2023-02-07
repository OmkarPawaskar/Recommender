import datetime
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Q
from django.utils import timezone

from ratings.models import Rating
# Create your models here.

RATING_CALC_TIME_IN_DAYS = 3    

class MovieQuerySet(models.QuerySet):
    def needs_updating(self):
        now = timezone.now()
        days_ago = now - datetime.timedelta(days=RATING_CALC_TIME_IN_DAYS)
        return self.filter(
            Q(rating_last_updated__isnull=True)|   # Q-> Encapsulate filters as objects that can then be combined logically (using & and |).
            Q(rating_last_updated__lte=days_ago)
        )

class MovieManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return MovieQuerySet(self.model, using=self._db)

    def needs_updating(self):
        return self.get_queryset().needs_updating()

class Movie(models.Model):

    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField()
    release_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    ratings = GenericRelation(Rating) #queryset
    rating_last_updated = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    rating_count = models.IntegerField(null=True, blank=True)
    rating_avg = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True) #5.00, 0d.00
    objects = MovieManager()

    def rating_avg_display(self):
        now = timezone.now()
        if not self.rating_last_updated:
            return self.calculate_rating()
        if self.rating_last_updated > now - datetime.timedelta(minutes=RATING_CALC_TIME_IN_DAYS):
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
        if not self.release_date:
            return self.title
        return f"{self.title} ({self.release_date.year})"