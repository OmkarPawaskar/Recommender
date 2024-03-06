import os
import sys
import dotenv
dotenv.load_dotenv()

DJANGO_SETTINGS_MODULE = "home.settings"


PWD = os.getenv("PWD")



def init():
    os.chdir(PWD)
    sys.path.insert(0, os.getenv("PWD"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django
    django.setup()