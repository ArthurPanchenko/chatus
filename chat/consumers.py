import json
import datetime

from channels.generic.websocket import WebsocketConsumer

from .models import ChatMessage, Chat


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        json_data = json.loads(text_data)
        message = ChatMessage.objects.create(
            author=self.scope['user'],
            text=json_data['message'],
            chat=Chat.objects.get(uuid=self.scope['url_route']['kwargs']['uuid'])
        )
        
        self.send(json.dumps({
            'author': message.author.username,
            'text': message.text,
            'date': f'{message.created.strftime('%d %m %Y')}'
        }))
    