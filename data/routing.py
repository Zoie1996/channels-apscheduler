from django.conf.urls import url

from . import consumers

# 配置WebSocket路由
websocket_urlpatterns = [
    url(r'^ws/data/$', consumers.DateConsumer),
]
