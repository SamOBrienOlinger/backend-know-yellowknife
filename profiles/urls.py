from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile-list'),  # List all profiles or create a new one
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),  # Retrieve, update, or delete a specific profile
]
