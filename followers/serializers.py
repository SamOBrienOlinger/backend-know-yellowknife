from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    profile_name = serializers.CharField(source="profile.owner.username", read_only=True)
    followed_name = serializers.CharField(source="followed_profile.owner.username", read_only=True)

    class Meta:
        model = Follower
        fields = ["id", "profile", "profile_name", "followed_profile", "followed_name", "created_at"]
        read_only_fields = ["id", "profile_name", "followed_name", "created_at"]
