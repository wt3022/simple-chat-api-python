from rest_framework.routers import SimpleRouter

from src.chats.views import ChatMessageViewSet


router = SimpleRouter()
router.register("", ChatMessageViewSet, basename="ChatMessages")

urlpatterns = router.urls
