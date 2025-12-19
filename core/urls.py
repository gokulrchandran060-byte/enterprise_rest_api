from django.urls import path
from .views import (
    HealthCheckAPIView,
    EchoAPIView,
    MessageCreateAPIView
)

urlpatterns = [
    path('health/', HealthCheckAPIView.as_view()),
    path('echo/', EchoAPIView.as_view()),
    path('messages/', MessageCreateAPIView.as_view()),
]
