import os
from celery import Celery
from .settings import CELERY_RESULT_BACKEND


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')

app = Celery("config")

app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()

app.conf.result_backend = CELERY_RESULT_BACKEND

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")