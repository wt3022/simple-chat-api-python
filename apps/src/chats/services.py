from datetime import datetime

from django.db.models import QuerySet

from src.chats.models import ChatMessage


def get_new_messages(timestamp: datetime) -> QuerySet[ChatMessage]:
    return ChatMessage.objects.filter(created_at__gte=timestamp)
