#https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from movies.tasks import task_calculate_movie_ratings



User = get_user_model()

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("count", nargs='?', default=1_000 ,type=int) # Positional arguments
        parser.add_argument("--all", action="store_true", default=False) # Named (optional) arguments

    def handle(self, *args, **options):
        count = options.get("count")
        all = options.get('all')
        task_calculate_movie_ratings(all=all, count=count)

        