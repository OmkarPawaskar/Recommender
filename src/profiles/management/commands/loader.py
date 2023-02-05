#https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from home import utils as home_utils
from movies.models import Movie

User = get_user_model()

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("count", nargs='?', default=10 ,type=int) # Positional arguments
        parser.add_argument("--movies", action="store_true", default=False)
        parser.add_argument("--users", action="store_true", default=False)
        parser.add_argument("--show-total", action="store_true", default=False) # Named (optional) arguments

    def handle(self, *args, **options):
        count = options.get("count")
        show_total = options.get("show_total")
        load_movies = options.get("movies")
        generate_users = options.get("users")

        if load_movies:
            movies_dataset = home_utils.load_movie_data(limit=count)
            movies_new = [Movie(**x) for x in movies_dataset]
            movies_bulk = Movie.objects.bulk_create(movies_new, ignore_conflicts=True)
            print(f"New movies : {len(movies_bulk)}")

            if show_total:
                print(f"Total movies : {Movie.objects.count()}")

        if generate_users:
            profiles = home_utils.get_fake_profiles(count=count)
            new_users = []
            
            for profile in profiles:
                new_users.append(
                    User(**profile)
                )
            
            user_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)
            print(f"New users : {len(user_bulk)}")

            if show_total:
                print(f"Total users : {User.objects.count()}")