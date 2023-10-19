from allauth.account.models import EmailAddress
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


def register_social_user(provider, user_id, email, name):
    email_check = User.objects.filter(email=email).first()
    if email_check is not None:
        registered_user = authenticate(
            username=email_check.username, password=user_id)
        if registered_user:
            refresh = RefreshToken.for_user(registered_user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            raise AuthenticationFailed(
                detail='Your data is not match to login using ' + provider)
    else:
        user_data = {
            'email': email,
            'name': name,
            'password': user_id}
        user = User.objects.create(**user_data)
        EmailAddress.objects.create(user=user, email=user.email, primary=True, verified=True)
        new_user = authenticate(
            username=user.username, password=user_id)
        if new_user:
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            raise AuthenticationFailed(
                detail='Please login again.')
