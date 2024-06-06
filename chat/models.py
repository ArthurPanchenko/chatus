import uuid

from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class Chat(models.Model):
    title = models.CharField(max_length=30, null=True)
    uuid = models.UUIDField(default=uuid.uuid4())
    participants = models.ManyToManyField(User, related_name='chats', through='ChatParticipants')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']

    def get_last_message(self):
        return self.messages.last()


class ChatParticipants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)


class ChatMessage(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        ordering = ['created']
