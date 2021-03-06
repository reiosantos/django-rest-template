# noinspection PyUnresolvedReferences
import os

from django_rest_template.settings import *

DEBUG = True

os.putenv('ELASTIC_APM_DISABLE_SEND', True)

SECRET_KEY = "SOMETHINGREALLYRANDOM"

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'USER': 'root',
		'PASSWORD': 'root',
		'NAME': 'django_rest_template_test',
		'HOST': 'db',
		'PORT': '3306',
		'OPTIONS': {
			'sql_mode': 'STRICT_TRANS_TABLES',
		}
	}
}

PSP_DASHBOARD_URL = 'https://test-%s.djangoresttemplate.com/dashboard/'
# url actually does not exist

PSP_REST_API_BASE_URL = 'http://localhost/'

ELASTICSEARCH_DSL = {
	'default': {
		'hosts': 'http://es01:9200'
	},
}
