"""
Commands
celery -A tasks worker --loglevel=info
"""


from celery import Celery


app = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/1')


@app.task(name='celery_worker.tasks.event')
def event(data):
    print('Recieved data', data)
    return data
