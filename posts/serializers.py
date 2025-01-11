from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    profile_name = serializers.CharField(source="profile.owner.username", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "profile", "profile_name", "content", "image", "created_at"]
        read_only_fields = ["id", "profile_name", "created_at"]
