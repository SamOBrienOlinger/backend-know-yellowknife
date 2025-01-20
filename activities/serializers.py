from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'profile', 'community_affiliations', 'favorite_things', 'community_insights']
        read_only_fields = ['id', 'profile']
