import requests
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings

from shower.users.models import User as UserType

from rest_framework import serializers
from .register import register_social_user

User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password')  # Include other required fields as well

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # Add more custom claims if needed
        return token



class GoogleSocialAuthSerializer(serializers.Serializer):
    code = serializers.CharField()

    def get_user_data(self, code):
        token_data = {
            'code': code,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri': "http://localhost:3000",
            'grant_type': 'authorization_code'
        }
        token_url = 'https://oauth2.googleapis.com/token'
        token_response = requests.post(token_url, data=token_data)

        access_token = token_response.json()['access_token']
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def validate_auth_token(self, auth_token):
        user_data = self.get_user_data(auth_token)
        if user_data:
            user_id = user_data['id']
            email = user_data['email']
            name = user_data['name']
            provider = 'google'
            return register_social_user(
                provider=provider,
                user_id=user_id,
                email=email,
                name=name)
        else:
            raise serializers.ValidationError(
                'The token  is invalid or expired. Please login again.'
            )
