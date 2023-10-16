from django.urls import path

from shower.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

from django.urls import path
from .api.views import GoogleSocialAuthView, FacebookSocialAuthView, TwitterSocialAuthView, LinkedInSocialAuthView


app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),

    # API
    path('google/', GoogleSocialAuthView.as_view()),
    path('facebook/', FacebookSocialAuthView.as_view()),
]
