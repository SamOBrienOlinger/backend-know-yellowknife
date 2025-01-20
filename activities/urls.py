from django.urls import path
from .views import ActivityDetail

urlpatterns = [
    path('my-activities/', ActivityDetail.as_view(), name='my-activities'),
]
