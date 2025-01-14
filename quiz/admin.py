from django.contrib import admin
from .models import QuizScore

@admin.register(QuizScore)
class QuizScoreAdmin(admin.ModelAdmin):
    list_display = ('profile', 'score', 'date_taken')  # Display these fields in the admin list view
    search_fields = ('profile__owner__username', 'score')  # Enable searching by username and score
    list_filter = ('date_taken',)  # Enable filtering by the date the quiz was taken

