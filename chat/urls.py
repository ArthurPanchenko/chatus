from django.urls import path

from . import views


urlpatterns = [
    path('', views.LobbyList.as_view(), name='lobby'),
    path('create-chat/', views.CreateChatView.as_view(), name='create_chat'),
    path('<uuid:uuid>/', views.ChatView.as_view(), name='chat'),
]