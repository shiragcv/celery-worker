"""
Commands
celery -A tasks worker --loglevel=info
"""


import time
from celery import Celery
from billiard import process


# celery = Celery(
#     'tasks',
#     broker='redis://redis:6379/0',
#     backend='redis://redis:6379/1')
celery = Celery(
    'tasks',
    broker='amqp://rabbitmq:5672',
    backend='amqp://rabbitmq:5672')


@celery.task(name='celery_worker.tasks.event')
def event(data):
    hostname = data.get("hostname") 
    current_process = process.current_process()

    return f'{hostname} -- {current_process.name}'
