from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer

class ProfileListView(generics.ListCreateAPIView):
    """
    Handles listing all profiles and creating a new profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Ensure the user can only access their own profile if updating or deleting.
        """
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return self.queryset.filter(owner=self.request.user)
        return super().get_queryset()

