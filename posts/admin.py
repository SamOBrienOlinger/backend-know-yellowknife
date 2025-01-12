from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('profile', 'content', 'created_at')  # Use 'profile'
    search_fields = ('profile__owner__username', 'title', 'content')  # Use 'profile__owner__username'
    list_filter = ('profile', 'created_at')


