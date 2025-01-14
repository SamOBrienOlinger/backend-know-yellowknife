from django.db import models
from profiles.models import Profile
from posts.models import Post

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()  # Ensure this matches the field name
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.owner}'s comment on {self.post.title}"
