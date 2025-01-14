from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'owner_username', 'created_at', 'updated_at', 'name', 'content', 'image']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
