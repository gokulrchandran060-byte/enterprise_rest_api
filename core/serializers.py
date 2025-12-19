from rest_framework import serializers
from .models import Message


class EchoSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=100)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'created_at']
