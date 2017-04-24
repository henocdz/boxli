from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['boxli-api.herokuapp.com']

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
