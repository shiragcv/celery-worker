"""
Commands
celery -A tasks worker --loglevel=info
"""


import time
from celery import Celery
from billiard import process


celery = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/1')


@celery.task(name='celery_worker.tasks.event')
def event(data):
    return f'{data.get("hostname")} -- {process.current_process()}'
