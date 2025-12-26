from django.urls import path
from .views import (
    HealthCheckAPIView,
    EchoAPIView,
    UserRegistrationAPIView,
    MessageCreateAPIView,
    MessageListAPIView,
)

urlpatterns = [
    path('health/', HealthCheckAPIView.as_view()),
    path('echo/', EchoAPIView.as_view()),
    path('register/', UserRegistrationAPIView.as_view()),
    path('messages/', MessageCreateAPIView.as_view()),
    path('messages/all/', MessageListAPIView.as_view()),
]
