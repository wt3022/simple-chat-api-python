from rest_framework import serializers

from src.accounts.serializers import UserSerializer
from src.chats.models import ChatMessage


class ChatMessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = ChatMessage
        fields = "__all__"
