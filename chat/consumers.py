import json
import datetime

from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync

from .models import ChatMessage, Chat

from channels_redis.core import RedisChannelLayer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['uuid']
        self.room_group_name = f'chat_{self.room_name}'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()


    def receive(self, text_data):
        json_data = json.loads(text_data)
        message = ChatMessage.objects.create(
            author=self.scope['user'],
            text=json_data['message'],
            chat=Chat.objects.get(uuid=self.scope['url_route']['kwargs']['uuid'])
        )

        print(message.created)

        respond_data = json.dumps({
            'author': message.author.username,
            'text': message.text,
            'date': f'{message.created.strftime('%d %B %Y г. %H:%M')}'
        })

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": respond_data}
        )
    
    def chat_message(self, event):
        message = event['message']

        self.send(text_data=message)
    