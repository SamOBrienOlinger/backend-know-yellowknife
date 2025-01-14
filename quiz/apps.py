from django.apps import AppConfig

class QuizConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz'
    verbose_name = "Quiz"  # This name will appear in the Django admin interface
