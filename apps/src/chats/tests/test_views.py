from django.utils import timezone
from factory.django import DjangoModelFactory
import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from src.accounts.models import User
from src.chats.views import ChatMessageViewSet


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User


@pytest.mark.django_db
class TestAPIViewTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ChatMessageViewSet.as_view({"get": "list", "post": "create"})
        self.test_user = UserFactory()

    def test_get_list(self):
        client_latest_timestamp_str = timezone.now().isoformat()

        url = reverse("ChatMessages-list")
        request = self.factory.get(url, {"latest_timestamp": client_latest_timestamp_str})
        force_authenticate(request, user=self.test_user)
        response = self.view(request)

        self.assertEqual(response.status_code, 200)
