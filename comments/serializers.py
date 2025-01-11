from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    profile_name = serializers.CharField(source="profile.owner.username", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "profile", "profile_name", "post", "content", "created_at"]
        read_only_fields = ["id", "profile_name", "created_at"]
