# urls.py
from django.urls import path
from .views import BusinessCreateAPIView, BusinessListView, CategoryView

urlpatterns = [
    path('create/', BusinessCreateAPIView.as_view(), name='create-business'),
    path('list/', BusinessListView.as_view(), name='list-business'),
    path("categories/", CategoryView.as_view(), name='list-category'),
]
