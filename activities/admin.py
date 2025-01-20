from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('profile', 'community_affiliations', 'favorite_things', 'community_insights')
    search_fields = ('profile__owner__username', 'community_affiliations', 'favorite_things')
