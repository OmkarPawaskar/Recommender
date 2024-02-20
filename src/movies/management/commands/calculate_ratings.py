#https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from ratings.tasks import task_update_movie_ratings

User = get_user_model()

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        task_update_movie_ratings()
        