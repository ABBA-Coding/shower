from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, PriceList
from .serializers import PriceListSerializer, OrderCreateSerializer, OrderListSerializer
from ..businesses.models import Business


class PriceListView(generics.ListAPIView):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer


class OrderListView(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        business_qs = Business.objects.filter(user=user)
        if business_qs.exists():
            business_obj = business_qs.first()
            qs = Order.objects.filter(campaign__business_id=business_obj.pk)
        else:
            qs = Order.objects.none()
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)


class ApironeCallbackView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        invoice = data.get('invoice')
        status = data.get('status')
        try:
            order = Order.objects.get(invoice_id=invoice)
            if status in ['paid', 'overpaid', 'completed']:
                order.status = Order.OrderStatusChoices.PAID
            elif status == "expired":
                order.status = Order.OrderStatusChoices.EXPIRED
            else:
                order.status = Order.OrderStatusChoices.PARTPAID
            order.save()
            return Response(status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
