import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY
# Use environment variable if set (on Render), else fallback for local dev
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-fallback-key-1234567890')

# DEBUG
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# ALLOWED_HOSTS
# Use environment variable if set, else allow localhost for dev
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1 localhost movie_clone_for_deploy_test-1.onrender.com').split(' ')

# Application definition
INSTALLED_APPS = [
    'tv.apps.TvConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TrackTV.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TrackTV.wsgi.application'

# Database
# Use DATABASE_URL from Render if set, else fallback to local SQLite
DATABASES = {
    "default": dj_database_url.parse(
        os.environ.get(
            "DATABASE_URL",
            f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}"
        )
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'

# Collect static files to a folder Render can serve
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra settings for crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login redirect
LOGIN_REDIRECT_URL = 'tv-home'
LOGIN_URL = '/login'
