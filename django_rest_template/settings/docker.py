# noinspection PyUnresolvedReferences
import os

from django_rest_template.settings import *

ALLOWED_HOSTS = ['*']

PSP_DASHBOARD_URL = 'http://local.djangoresttemplate.com/dashboard/'
PSP_REST_API_BASE_URL = 'http://local.djangoresttemplate.com/api/'

SSL_ENABLED = False

ELASTIC_APM['SERVICE_NAME'] = 'rest_api_docker'
ELASTIC_APM['DEBUG'] = True

# INSTALLED_APPS += (
# 	'silk',
# )

# MIDDLEWARE = ('silk.middleware.SilkyMiddleware',) + MIDDLEWARE

SILKY_META = True
SILKY_PYTHON_PROFILER = True

SILKY_DYNAMIC_PROFILING = []
