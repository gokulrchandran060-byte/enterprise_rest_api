from django.urls import path
from .views import (
    HealthCheckAPIView,
    EchoAPIView,
    MessageCreateAPIView,
    MessageListAPIView,
    UserRegistrationAPIView,
)

urlpatterns = [
    # Health & utility
    path('health/', HealthCheckAPIView.as_view(), name='health-check'),
    path('echo/', EchoAPIView.as_view(), name='echo'),

    # Auth
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),

    # Messages
    path('messages/', MessageCreateAPIView.as_view(), name='message-create'),
    path('messages/all/', MessageListAPIView.as_view(), name='message-list'),
]
