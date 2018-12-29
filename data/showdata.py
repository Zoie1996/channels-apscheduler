import os
import random

import django
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eg_channels.settings')
django.setup()


def showdata():
    # 访问数据库操作
    # 外部获取用户模型
    user = get_user_model()
    # 获取最后插入的用户id
    last_user_id = user.objects.all().order_by("-id").first().id
    # 使用随机数模拟阿胡局变化
    day = [random.randint(1, 15) for _ in range(3)]
    month = [random.randint(1, 30) for _ in range(3)]
    # 外部获取通道层
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "data",
        {
            "type": "data_message",
            "id": last_user_id,
            "day": day,
            "month": month,
        }
    )
