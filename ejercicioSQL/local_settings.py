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


BASEURL = 'localhost:8000'

APIS = {
    'authentication': 'localhost:8000',
}