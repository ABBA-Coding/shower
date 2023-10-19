from django.contrib.auth import get_user_model
from rest_framework import status, serializers
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer, UserRegisterSerializer
from .serializers import CustomTokenObtainPairSerializer
from .serializers import GoogleSocialAuthSerializer



User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class GoogleSocialAuthView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        auth_token = serializer.validated_data['code']

        try:
            # user = serializer.validate_auth_token(auth_token)
            user = serializer.get_user_data(auth_token)
            return Response(user, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

