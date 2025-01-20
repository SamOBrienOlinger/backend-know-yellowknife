from rest_framework import generics, permissions
from .models import Activity
from .serializers import ActivitySerializer
from profiles.models import Profile

class ActivityDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Ensure only the authenticated user's activity is accessed
        profile = Profile.objects.get(owner=self.request.user)
        activity, created = Activity.objects.get_or_create(profile=profile)
        return activity

