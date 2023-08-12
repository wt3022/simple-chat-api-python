from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer


class LoginSerializer(DefaultLoginSerializer):
    username = None
