import random

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class DateConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)("data", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("data", self.channel_name)

    # def receive(self, text_data):
    #     async_to_sync(self.channel_layer.group_send)(
    #         "data",
    #         {
    #             "type": "data_message",
    #             "text": text_data,
    #         },
    #     )

    def data_message(self, event):
        # 发送数据到WebSocket

        self.send(text_data=json.dumps(event))
