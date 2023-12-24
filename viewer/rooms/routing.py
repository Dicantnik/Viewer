from django.urls import path
from . import consumers

websocket_urlpatterns =[
    path('ws/<str:code>/', consumers.RoomConsumer.as_asgi()),
]