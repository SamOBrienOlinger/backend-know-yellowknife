from django.db import models
from profiles.models import Profile



class Follower(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="followers_from_followers")
    followed_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="following_from_followers")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.owner} follows {self.followed_profile.owner}"
