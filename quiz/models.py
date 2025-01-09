from django.db import models
from profiles.models import Profile

class QuizScore(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='quiz_scores')
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_taken']

    def __str__(self):
        return f"{self.profile.owner}'s quiz score: {self.score}"

