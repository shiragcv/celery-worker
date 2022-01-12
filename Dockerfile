FROM python:3.10.1-alpine
WORKDIR '/user/app'
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src .
CMD ["celery", "-A", "celery_worker.tasks", "worker", "--loglevel=info"]
