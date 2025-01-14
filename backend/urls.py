from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/social/', include('social.urls')),  # Include the social app's URLs
    path('api/profiles/', include('profiles.urls')),  # Include the profiles app's URLs (if not already added)
    path('api-auth/', include('rest_framework.urls')),  # Optional: for API authentication
]

