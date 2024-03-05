import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres_injection',
        'USER': 'postgres_injection',
        'PASSWORD': 'postgres_injection',
        'HOST': 'db',
        'PORT': 5432,
    }
}


BASEURL = 'http://10.5.0.1:8000'

APIS = {
    'authentication': 'http://10.5.0.1:8000',
}