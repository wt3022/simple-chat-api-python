from dj_rest_auth.views import LoginView
from dj_rest_auth.views import LogoutView
from django.urls import include
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
]

urlpatterns += [
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
