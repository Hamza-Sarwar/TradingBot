from django.urls import path
from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/abc_urls/', WSConsumer.as_asgi()),
]