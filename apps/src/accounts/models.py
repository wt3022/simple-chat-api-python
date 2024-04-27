import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from src.utils.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=True)
