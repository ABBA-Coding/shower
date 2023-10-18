# urls.py
from django.urls import path
from .views import BusinessCreateAPIView, BusinessListView, CategoryView, BusinessWithoutAuthListView

urlpatterns = [
    path('create/', BusinessCreateAPIView.as_view(), name='create-business'),
    path('list/', BusinessListView.as_view(), name='list-business'),
    path('without-auth-list/', BusinessWithoutAuthListView.as_view(), name='list-business'),
    path("categories/", CategoryView.as_view(), name='list-category'),
]
