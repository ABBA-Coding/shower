from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Campaign
from .serializers import CampaignUpdateSerializer, CampaignListSerializer, CampaignCreateSerializer


class CampaignListView(generics.ListAPIView):
    serializer_class = CampaignListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Campaign.objects.filter(business__user=user).select_related("business")


class CampaignListWithoutAuthView(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignListSerializer


class CampaignRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignUpdateSerializer


class CampaignCreateView(generics.CreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignCreateSerializer

