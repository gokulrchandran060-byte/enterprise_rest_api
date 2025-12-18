from django.urls import path
from .views import HealthCheckAPIView, EchoAPIView

urlpatterns = [
    path('health/', HealthCheckAPIView.as_view()),
    path('echo/', EchoAPIView.as_view()),
]
