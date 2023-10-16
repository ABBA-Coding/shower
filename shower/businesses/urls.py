# urls.py
from django.urls import path
from .views import BusinessCreateAPIView, BusinessListView

urlpatterns = [
    path('create/', BusinessCreateAPIView.as_view(), name='create-business'),
    path('list/', BusinessListView.as_view(), name='list-business'),
]
