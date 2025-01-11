from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    profile_name = serializers.CharField(source="profile.owner.username", read_only=True)

    class Meta:
        model = Like
        fields = ["id", "profile", "profile_name", "post", "created_at"]
        read_only_fields = ["id", "profile_name", "created_at"]
