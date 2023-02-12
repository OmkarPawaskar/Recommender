import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

app = Celery('home')

#CELERY
app.config_from_object('django.conf:settings', namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "run_movie_rating_every_30": {
        'task' : 'task_calculate_movie_ratings',
        'schedule' : 60*30, #30 mins
        'kwargs' : {"count" : "20_000"}
    }
}

