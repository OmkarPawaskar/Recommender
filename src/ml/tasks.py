from celery import shared_task

from . import utils as ml_utils

@shared_task
def train_surpirse_model_task():
    ml_utils.train_surprise_model()