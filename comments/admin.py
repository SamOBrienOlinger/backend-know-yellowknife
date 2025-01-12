from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('profile', 'post', 'content', 'created_at')  # Use 'profile' instead of 'user'
    search_fields = ('profile__owner__username', 'post__title')  # Use 'profile__owner__username'
    list_filter = ('created_at',)

