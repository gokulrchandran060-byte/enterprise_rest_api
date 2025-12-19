print(">>> CORE VIEWS FILE LOADED <<<")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import EchoSerializer, MessageSerializer
from .models import Message
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated

class HealthCheckAPIView(APIView):
    def get(self, request):
        return Response(
            {"status": "ok", "message": "Server is running"},
            status=status.HTTP_200_OK
        )


class EchoAPIView(APIView):
    def post(self, request):
        serializer = EchoSerializer(data=request.data)

        if serializer.is_valid():
            return Response(
                {"echo": serializer.validated_data["message"]},
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class MessageCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

