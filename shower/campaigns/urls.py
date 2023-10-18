from django.urls import path
from . import views

urlpatterns = [
    path('me-list/', views.CampaignListView.as_view(), name='campaign-list'),
    path('all-list/', views.CampaignListWithoutAuthView.as_view(), name='campaign-all-list'),
    path('create/', views.CampaignCreateView.as_view(), name='campaign-create'),
    path('<int:pk>/', views.CampaignRetrieveUpdateDestroyView.as_view(), name='campaign-detail'),
]
