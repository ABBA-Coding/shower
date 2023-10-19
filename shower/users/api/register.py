from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


def register_social_user(provider, user_id, email, name):
    user_qs = User.objects.filter(email=email)
    if user_qs.exists():
        user = user_qs.first()
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    else:
        user_data = {
            'email': email,
            'name': name,
            'password': user_id}
        user = User.objects.create(**user_data)
        if user:
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            raise AuthenticationFailed(
                detail='Please login again.')
