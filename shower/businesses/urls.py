# urls.py
from django.urls import path
from .views import BusinessCreateAPIView, BusinessMeView, CategoryView, BusinessWithoutAuthListView

urlpatterns = [
    path('create/', BusinessCreateAPIView.as_view(), name='create-business'),
    path('me/', BusinessMeView.as_view(), name='me-business'),
    path('without-auth-list/', BusinessWithoutAuthListView.as_view(), name='list-business'),
    path("categories/", CategoryView.as_view(), name='list-category'),
]
