"""voyage_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import re_path, path
from django.views.static import serve
from rest_framework_jwt import views
from rest_framework_swagger.views import get_swagger_view

from django_rest_template.apps.common.handlers import (
	psp_page_not_found,
	psp_bad_request,
	psp_permission_denied,
	psp_server_error
)
from django_rest_template.apps.common.views import HealthCheckView

schema_view = get_swagger_view(title='Django Rest API')

urlpatterns = [
	path('grappelli/', include('grappelli.urls')),  # disabled for now
	path('admin/', admin.site.urls),
	path('accounts/', include('rest_framework.urls', namespace='rest_framework')),
	path('jwt/login/', views.obtain_jwt_token),
	path('jwt/verify/', views.verify_jwt_token),
	path('health/', HealthCheckView.as_view({'get': 'get'}), name='health_check'),
	path('docs/', schema_view),
	path(
		'password/change/',
		login_required(auth_views.PasswordChangeView.as_view()), name='password_change'),
	path(
		'password/change/done/',
		login_required(auth_views.PasswordChangeDoneView.as_view()), name='password_change_done'),
	path('password/reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path(
		'password/reset/done/',
		auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	re_path(
		r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path(
		'reset/done/',
		auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

	# Done with general routes
	path(
		'permission/',
		include('django_rest_template.apps.permission.urls', namespace='permission')),
	path(
		'terminology/',
		include('django_rest_template.apps.terminology.urls', namespace='terminology')),
	path('email/', include('django_rest_template.apps.email.urls', namespace='email')),
	path('oauth/', include('django_rest_template.apps.oauth.urls', namespace='oauth')),
	path('user/', include('django_rest_template.apps.user.urls', namespace='user')),
	path('venue/', include('django_rest_template.apps.venue.urls', namespace='venue')),
]

# @TODO in production, serve files differently
urlpatterns += [
	re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
	re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]

if 'silk' in settings.INSTALLED_APPS:
	urlpatterns += [
		path('silk/', include('silk.urls', namespace='silk'))
	]

handler400 = psp_bad_request
handler404 = psp_page_not_found
handler403 = psp_permission_denied
handler500 = psp_server_error
