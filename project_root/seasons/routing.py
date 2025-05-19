from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/likes/index/', consumers.LikeConsumer.as_asgi()),
]