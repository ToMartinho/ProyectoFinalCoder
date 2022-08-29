import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message':' Esta Conectado'
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        usuario = text_data_json['usuario']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'usuario':usuario,
            }
        )
    def chat_message(self, event):
        message = event['message']
        usuario = event['usuario']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'usuario':usuario,
            }))