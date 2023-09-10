from datetime import datetime
import time

from django.utils import timezone
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from src import env
from src.chats.models import ChatMessage
from src.chats.serializers import ChatMessageSerializer
from src.chats.services import get_new_messages


@extend_schema_view(
    list=extend_schema(
        parameters=[OpenApiParameter("latest_timestamp", OpenApiTypes.DATETIME, OpenApiParameter.QUERY, required=True)]
    )
)
class ChatMessageViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def list(self, request, *args, **kwargs):
        client_latest_timestamp = datetime.fromisoformat(request.query_params.get("latest_timestamp"))

        if not client_latest_timestamp:
            raise ValidationError({"latestTimestamp": "この値は必須です。"})

        timeout = env.LONG_POLLING_TIMEOUT_SECONDS
        start_time = timezone.localtime()

        while (timezone.localtime() - start_time).seconds <= timeout:
            queryset = get_new_messages(client_latest_timestamp)
            if queryset.exists():
                serializer = self.get_serializer(self.paginate_queryset(queryset), many=True)
                return Response(serializer.data)

            time.sleep(env.LONG_POLLING_LOOP_DELAY_SECONDS)

        return super().list(request, *args, **kwargs)
