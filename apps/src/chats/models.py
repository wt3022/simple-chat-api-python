from django.db import models

from src.utils.models import CurrentUserField


class ChatMassage(models.Model):
    text = models.TextField("テキスト", max_length=2048)
    created_at = models.DateTimeField("作成日時", auto_now=True)
    created_by = CurrentUserField(verbose_name="投稿者")
