from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['boxli-api.herokuapp.com', 'api.boxli.co', 'boxli.co', 'bxli.co']

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

SITE_URL = 'http://{}/'.format(os.getenv('BOXLI_SITE_URL'))
