from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('profile', 'post', 'text', 'created_at')  # Ensure 'text' matches the field in the model
    search_fields = ('profile__owner__username', 'post__title')  # Ensure valid search fields
    list_filter = ('created_at',)
