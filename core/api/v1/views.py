print(">>> CORE VIEWS FILE LOADED <<<")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from core.models import Message
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from core.services.message_service import create_message
from core.responses import success_response
from core.permissions import CanViewAllMessages
from core.serializers import (
    MessageSerializer,
    EchoSerializer,
    UserRegistrationSerializer,
)


class MessageListAPIView(APIView):
    permission_classes = [CanViewAllMessages]

    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)



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

        print("HEADERS:", request.headers)
        print("AUTH:", request.META.get("HTTP_AUTHORIZATION"))
        print("USER:", request.user)



        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = create_message(serializer.validated_data["content"])
        return success_response(
            MessageSerializer(message).data,
            status=201
        )






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

