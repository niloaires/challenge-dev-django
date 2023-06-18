from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'propostas.settings')
app = Celery('propostas')

app.conf.broker_url = 'amqp://guest:guest@rabbitmq:5672//'
app.conf.result_backend = 'rpc://'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
