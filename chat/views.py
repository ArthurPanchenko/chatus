from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from django.urls import reverse

from .models import Chat, ChatMessage, ChatParticipants
from .forms import CreateChatForm
from .utils import add_participant_to_chat


class LobbyList(ListView):
    model = Chat
    template_name = 'chat/lobby.html'
    context_object_name = 'chats'

    def get_queryset(self):
        return self.request.user.chats.all()


class ChatView(ListView):
    model = ChatMessage
    template_name = 'chat/chat.html'
    context_object_name = 'chat'
    
    def get_queryset(self):
        return Chat.objects.prefetch_related('messages').get(uuid=self.kwargs['uuid'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chat_title'] = Chat.objects.get(uuid=self.kwargs['uuid'])
        return context


class CreateChatView(FormMixin, TemplateView):
    template_name = 'chat/create_chat.html'
    form_class = CreateChatForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            chat = form.save()
            add_participant_to_chat(chat, request.user, is_owner=True)
            return redirect(reverse('chat', kwargs={'uuid': chat.uuid}))
