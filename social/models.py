from django.db import models
from profiles.models import Profile
from posts.models import Post

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments_from_social")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_from_social")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.profile.owner} on {self.post.title}"


class Follower(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="followers_from_social")
    followed_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="following_from_social")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.owner} follows {self.followed_profile.owner}"


class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="likes_from_social")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes_from_social")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.owner} likes {self.post.title}"


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts_from_social")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
