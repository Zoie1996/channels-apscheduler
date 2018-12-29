from celery import Celery

# 设置celery使用django配置文件
import os

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eg_channels.settings')

celery_app = Celery('eg_channels')

# 导入celery配置(wahaha.celery_tasks.config)
celery_app.config_from_object('django.conf:settings')

# 自动注册celery任务
celery_app.autodiscover_tasks(['celery_tasks.analytics'  # 自动从celery_tasks下的analytics中找到tasks文件
                               ])
