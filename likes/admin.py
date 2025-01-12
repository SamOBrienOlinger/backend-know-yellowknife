from django.contrib import admin
from .models import Like

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('profile', 'post', 'created_at')  # Use 'profile'
    search_fields = ('profile__owner__username', 'post__title')  # Use 'profile__owner__username'
    list_filter = ('created_at',)


