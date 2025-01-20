from django.db import models
from profiles.models import Profile

class Activity(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="activities")
    community_affiliations = models.TextField(
        blank=True,
        null=True,
        help_text="Community/communities the user identifies with."
    )
    favorite_things = models.TextField(
        blank=True,
        null=True,
        help_text="Top three things the user likes about Yellowknife."
    )
    community_insights = models.TextField(
        blank=True,
        null=True,
        help_text="What the user feels is important for other Yellowknifers to know about their community."
    )

    def __str__(self):
        return f"Activities for {self.profile.owner.username}"

