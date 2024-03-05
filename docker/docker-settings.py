import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres_injection',
        'USER': 'postgres_injection',
        'PASSWORD': 'postgres_injection',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
ALLOWED_HOSTS = ['*']

BASEURL = 'http://10.5.0.1:8000'

APIS = {
    'store': 'http://10.5.0.1:8000',
}