from rest_framework import generics, permissions
from .models import QuizScore
from .serializers import QuizScoreSerializer

class QuizScoreListCreateView(generics.ListCreateAPIView):
    """
    List all quiz scores or create a new quiz score.
    """
    queryset = QuizScore.objects.all()
    serializer_class = QuizScoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically associate the logged-in user's profile with the quiz score.
        """
        serializer.save(profile=self.request.user.profile)


class QuizScoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific quiz score.
    """
    queryset = QuizScore.objects.all()
    serializer_class = QuizScoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users can only access their own quiz scores.
        """
        return self.queryset.filter(profile=self.request.user.profile)

