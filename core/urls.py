print(">>> CORE URLS LOADED <<<")

from django.urls import path
from .views import (
    HealthCheckAPIView,
    EchoAPIView,
    MessageCreateAPIView,
    UserRegistrationAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('health/', HealthCheckAPIView.as_view()),
    path('echo/', EchoAPIView.as_view()),
    path('messages/', MessageCreateAPIView.as_view()),
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
