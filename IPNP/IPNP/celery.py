import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IPNP.settings')


app = Celery('IPNP')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'weekly_notifications': {
        'task': 'PortalApp.tasks.weekly_notifications_task',
        'schedule': crontab(hour='08', minute='00', day_of_week='monday'),
    },
}


app.autodiscover_tasks()
