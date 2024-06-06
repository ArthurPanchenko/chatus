from django.contrib import admin

from .models import Chat, ChatParticipants, ChatMessage


admin.site.register(Chat)
admin.site.register(ChatParticipants)
admin.site.register(ChatMessage)