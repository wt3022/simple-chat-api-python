from django.db import models
from django_currentuser.db.models import CurrentUserField

from src.utils.models import TimeStampedModel


class ChatMessage(TimeStampedModel):
    text = models.TextField("テキスト", max_length=2048)
    created_by = CurrentUserField(verbose_name="投稿者", on_update=True)

    class Meta:
        verbose_name = verbose_name_plural = "チャットメッセージ"
        ordering = ["created_at"]
