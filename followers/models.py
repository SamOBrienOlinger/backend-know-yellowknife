from django.db import models
from profiles.models import Profile

class Follower(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="following")
    followed_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["profile", "followed_profile"]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.profile.owner.username} follows {self.followed_profile.owner.username}"

