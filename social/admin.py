from django.contrib import admin
from .models import Post, Comment, Like, Follower


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('profile', 'title', 'created_at', 'updated_at')
    search_fields = ('profile__owner__username', 'title')
    list_filter = ('created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('profile', 'post', 'text', 'created_at')
    search_fields = ('profile__owner__username', 'post__title')
    list_filter = ('created_at',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('profile', 'post', 'created_at')
    search_fields = ('profile__owner__username', 'post__title')


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('profile', 'followed_profile', 'created_at')
    search_fields = ('profile__owner__username', 'followed_profile__owner__username')

