from django.db import models
from profiles.models import Profile
from posts.models import Post

class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["profile", "post"]
        ordering = ["-created_at"]

    def __str__(self):
        return f"Like by {self.profile.owner.username} on Post {self.post.id}"
