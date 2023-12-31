from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('list/', views.OrderListView.as_view(), name='order-list'),
    path('price-list/', views.PriceListView.as_view(), name='price-list'),
    path('apirone-callback/', views.ApironeCallbackView.as_view(), name='apirone-callback'),
]
