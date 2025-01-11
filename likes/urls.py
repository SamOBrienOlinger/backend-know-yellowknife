from django.urls import path
from .views import LikeListCreateView

urlpatterns = [
    path("", LikeListCreateView.as_view(), name="like-list-create"),
]
