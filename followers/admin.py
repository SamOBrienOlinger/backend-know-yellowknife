from django.contrib import admin
from .models import Follower

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('profile', 'followed_profile', 'created_at')  # Use 'profile' and 'followed_profile'
    search_fields = ('profile__owner__username', 'followed_profile__owner__username')  # Adjusted for 'Profile'
    list_filter = ('created_at',)


