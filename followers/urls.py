from django.urls import path
from .views import FollowerListCreateView

urlpatterns = [
    path("", FollowerListCreateView.as_view(), name="follower-list-create"),
]
