"""
Commands
celery -A tasks worker --loglevel=info
"""


import time
from celery import Celery


celery = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/1')


@celery.task(name='celery_worker.tasks.event')
def event(data):
    print('Recieved data', data)
    print('Computing data')
    time.sleep(10)
    print('Computation success')
    return 'Success'
