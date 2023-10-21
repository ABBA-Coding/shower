from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, PriceList
from .serializers import PriceListSerializer, OrderCreateSerializer


class PriceListView(generics.ListAPIView):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer


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
