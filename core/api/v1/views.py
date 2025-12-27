
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from core.models import Message
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User

from core.services.message_service import create_message
from core.responses import success_response
from core.permissions import CanViewAllMessages
from core.serializers import (
    MessageSerializer,
    EchoSerializer,
    UserRegistrationSerializer,
)
import logging
logger = logging.getLogger(__name__)




class MessageListAPIView(APIView):
    permission_classes = [CanViewAllMessages]

    def get(self, request):
        if not request.user.is_staff:
            logger.warning(f"Unauthorized message list access attempt by user_id={request.user.id}")
            raise PermissionDenied("Admin access required")

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
        logger.info(f"Message created | message_id={message.id} | user_id={request.user.id}")
        return success_response(
            MessageSerializer(message).data,
            status=201
        )


class MessageUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, message_id):
        try:
            message = Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            logger.error(f"Update failed: message_id={message_id} not found")
            return Response(
                {"detail": "Message not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MessageSerializer(
            message,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return success_response(serializer.data)

class MessageDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, message_id):
        try:
            message = Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            return Response(
                {"detail": "Message not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        message.delete()
        return success_response(
            {"message": "Deleted successfully"}
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

