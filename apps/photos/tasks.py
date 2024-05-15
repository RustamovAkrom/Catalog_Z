from celery import shared_task

@shared_task
def bar():
    return "Hello Workd!"