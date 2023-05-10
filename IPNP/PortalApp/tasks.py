from celery import shared_task
import time


@shared_task
def hello():
    time.sleep(10)
    print('Hello from tasks')


@shared_task
def printer(x):
    for i in range(x):
        time.sleep(1)
        print(i + 1)
