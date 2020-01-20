# noinspection PyUnresolvedReferences
from django_rest_template.settings import *

ALLOWED_HOSTS = ['*']

SERVER_EMAIL = 'stg-no-reply@djangoresttemplate.com'

DEFAULT_FROM_EMAIL = 'stg-info@djangoresttemplate.com'

PSP_DASHBOARD_URL = 'https://stg-%s.djangoresttemplate.com/dashboard/'

PSP_REST_API_BASE_URL = 'https://stg-api.djangoresttemplate.com/api/'

ELASTIC_APM['SERVICE_NAME'] = 'rest_api_staging'
