from rest_framework import serializers
from .models import Post, Comment, Like, Follower


class PostSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')  # Include owner's username
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')  # Profile image URL

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'owner_username', 'profile_image',
            'title', 'content', 'image', 'created_at', 'updated_at',
        ]


class CommentSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')  # Include owner's username
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')  # Profile image URL

    class Meta:
        model = Comment
        fields = [
            'id', 'post', 'owner', 'owner_username', 'profile_image',
            'text', 'created_at',
        ]


class LikeSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')  # Include owner's username

    class Meta:
        model = Like
        fields = [
            'id', 'post', 'owner', 'owner_username', 'created_at',
        ]


class FollowerSerializer(serializers.ModelSerializer):
    followed_username = serializers.ReadOnlyField(source='followed.username')  # Username of the followed user
    follower_username = serializers.ReadOnlyField(source='follower.username')  # Username of the follower

    class Meta:
        model = Follower
        fields = [
            'id', 'follower', 'follower_username', 'followed', 'followed_username', 'created_at',
        ]
