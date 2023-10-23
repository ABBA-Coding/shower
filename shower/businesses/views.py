from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shower.businesses.models import Business, Category
from shower.businesses.serializers import BusinessCreateSerializer, BusinessListSerializer, CategorySerializer, \
    BusinessDetailSerializer


class BusinessCreateAPIView(APIView):
    queryset = Business.objects.all()
    serializer_class = BusinessCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = BusinessCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            try:
                serializer.save()
            except:
                return Response({"detail": "Boshqa yaratib bo'lmaydi"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            return Response([], status.HTTP_200_OK)
        return Response(self.serializer_class(qs).data)


class BusinessWithoutAuthListView(generics.ListAPIView):
    serializer_class = BusinessListSerializer
    queryset = Business.objects.all()


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
