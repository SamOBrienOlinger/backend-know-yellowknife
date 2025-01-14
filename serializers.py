from rest_framework import serializers
from .models import Post, Comment, Like, Follower


class PostSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='profile.owner.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'profile', 'owner_username', 'title', 'content', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner_username', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='profile.owner.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'profile', 'owner_username', 'post', 'text', 'created_at']
        read_only_fields = ['id', 'owner_username', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='profile.owner.username', read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'profile', 'owner_username', 'post', 'created_at']
        read_only_fields = ['id', 'owner_username', 'created_at']


class FollowerSerializer(serializers.ModelSerializer):
    follower_username = serializers.CharField(source='profile.owner.username', read_only=True)
    followed_username = serializers.CharField(source='followed_profile.owner.username', read_only=True)

    class Meta:
        model = Follower
        fields = ['id', 'profile', 'follower_username', 'followed_profile', 'followed_username', 'created_at']
        read_only_fields = ['id', 'follower_username', 'followed_username', 'created_at']
