from rest_framework import generics

from .models import Campaign
from .serializers import CampaignUpdateSerializer, CampaignListSerializer, CampaignCreateSerializer


class CampaignListWithoutAuthView(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignListSerializer


class CampaignRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignUpdateSerializer


class CampaignCreateView(generics.CreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignCreateSerializer

