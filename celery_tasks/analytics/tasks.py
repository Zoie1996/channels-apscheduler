import logging
from channels.layers import get_channel_layer

from data.showdata import testdata
from ..main import celery_app

channel_layer = get_channel_layer()
logger = logging.getLogger()


@celery_app.task(name='showdata')  # 任务名
def showdata():
    testdata()

# 开启任务的命令
# celery -A celery_tasks.main worker -l info
