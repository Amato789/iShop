import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.iShop.settings.base')
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
