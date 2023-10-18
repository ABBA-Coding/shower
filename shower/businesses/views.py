from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shower.businesses.models import Business, Category
from shower.businesses.serializers import BusinessCreateSerializer, BusinessListSerializer, CategorySerializer, \
    BusinessDetailSerializer


class BusinessCreateAPIView(generics.CreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessCreateSerializer
    permission_classes = [IsAuthenticated]


class BusinessMeView(generics.ListAPIView):
    """Business list for authenticated user"""
    serializer_class = BusinessDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        qs = Business.objects.filter(user=user).prefetch_related("campaigns")
        if qs.exists():
            qs = qs.first()
        else:
            qs = Business.objects.none()
        return Response(self.serializer_class(qs).data)


class BusinessWithoutAuthListView(generics.ListAPIView):
    serializer_class = BusinessListSerializer
    queryset = Business.objects.prefetch_related("campaigns")


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
