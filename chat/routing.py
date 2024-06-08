from django.urls import re_path

from .consumers import ChatConsumer


ws_urlpatterns = [
    re_path(r'^chat/(?P<uuid>[^/]+)/$', ChatConsumer.as_asgi())
]