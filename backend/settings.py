from pathlib import Path
import os
import re
import dj_database_url

print("DATABASE_URL:", os.environ.get('DATABASE_URL'))

# Load environment variables
if os.path.exists('env.py'):
    import env

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key and Debug Mode
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allowed Hosts
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000', 'https://8000-samobrienol-backendknow-ow5rhbepic7.ws-eu117.gitpod.io',
]

# Dynamically add Gitpod or other environments to CSRF Trusted Origins
if 'CLIENT_ORIGIN' in os.environ:
    CSRF_TRUSTED_ORIGINS.append(os.environ.get('CLIENT_ORIGIN'))
if 'CLIENT_ORIGIN_DEV' in os.environ:
    client_origin_dev = os.environ.get('CLIENT_ORIGIN_DEV', '')
    if 'gitpod.io' in client_origin_dev:
        match = re.match(r'^https:\/\/\d+-', client_origin_dev)
        if match:
            extracted_url = f"{match.group(0)}{os.environ.get('GITPOD_WORKSPACE_URL').split('//')[-1]}"
            CSRF_TRUSTED_ORIGINS.append(extracted_url)
    else:
        CSRF_TRUSTED_ORIGINS.append(client_origin_dev)

# Cloudinary for Media Storage
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}

REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    os.environ.get('CLIENT_ORIGIN', ''),
]

CORS_ALLOW_CREDENTIALS = True

if 'CLIENT_ORIGIN_DEV' in os.environ:
    client_origin_dev = os.environ.get('CLIENT_ORIGIN_DEV', '')
    if 'gitpod.io' in client_origin_dev:
        match = re.match(r'^.+-', client_origin_dev, re.IGNORECASE)
        if match:
            extracted_url = match.group(0)
            CORS_ALLOWED_ORIGIN_REGEXES = [
                rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
            ]
        else:
            raise ValueError("CLIENT_ORIGIN_DEV is not in the expected Gitpod format.")
    else:
        # For localhost or other non-Gitpod setups
        CORS_ALLOWED_ORIGINS = [
            client_origin_dev,
        ]

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',
    'profiles',      # User profiles
    'posts',         # Posts (or "social" app)
    'comments',      # Comments on posts
    'likes',         # Likes on posts
    'followers',     # Followers and following system
]

SITE_ID = 1

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add directories for custom templates if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database Configuration
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Static Files
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Time Zone and Language
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
