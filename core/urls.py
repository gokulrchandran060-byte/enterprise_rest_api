print(">>> CORE URLS LOADED <<<")

from django.urls import path
from .views import (
    HealthCheckAPIView,
    EchoAPIView,
    MessageCreateAPIView,
    UserRegistrationAPIView
)


urlpatterns = [
    path('health/', HealthCheckAPIView.as_view()),
    path('echo/', EchoAPIView.as_view()),
    path('messages/', MessageCreateAPIView.as_view()),
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),

]
