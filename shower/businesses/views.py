from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from shower.businesses.models import Business, Category
from shower.businesses.serializers import BusinessCreateSerializer, BusinessListSerializer, CategorySerializer


class BusinessCreateAPIView(generics.CreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessCreateSerializer
    permission_classes = [IsAuthenticated]


class BusinessListView(generics.ListAPIView):
    serializer_class = BusinessListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Business.objects.filter(user=user)


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
