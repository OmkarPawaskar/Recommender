#https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from home import utils as home_utils

User = get_user_model()

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("count", nargs='?', default=10 ,type=int) # Positional arguments
        parser.add_argument("--show-total", action="store_true", default=False) # Named (optional) arguments

    def handle(self, *args, **options):
        count = options.get("count")
        show_total = options.get("show_total")
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