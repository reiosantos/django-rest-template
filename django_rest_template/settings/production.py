# noinspection PyUnresolvedReferences
from django_rest_template.settings import *

ADMINS = (
    ('Reio Santos', 'santos@djangoresttemplate.com'),
)

ALLOWED_HOSTS = ['*']

SERVER_EMAIL = 'no-reply@djangoresttemplate.com'
DEFAULT_FROM_EMAIL = 'info@djangoresttemplate.com'

# IMPORTANT On a production server, ensure that a unique key is generated
SECRET_KEY = ';i}xOSFlh2v+y-SsXl!)JnJ/7Kb(tOJH7J1=~z6c_{eSr,S;{l'

PSP_DASHBOARD_URL = 'https://%s.djangoresttemplate.com/dashboard/'

PSP_REST_API_BASE_URL = 'https://ecs-api.djangoresttemplate.com/api/'

ELASTIC_APM['SERVICE_NAME'] = 'rest_api_production'
