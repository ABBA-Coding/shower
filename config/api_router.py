from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from shower.users.api.views import UserViewSet, GoogleSocialAuthView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

app_name = "api"
urlpatterns = router.urls
urlpatterns += [
    path("business/", include("shower.businesses.urls"), name="business"),
    path("campaign/", include("shower.campaigns.urls"), name="campaign"),
    path("orders/", include("shower.orders.urls"), name="orders"),
    path('google/', GoogleSocialAuthView.as_view()),
]
