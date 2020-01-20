from django.urls import path

from django_rest_template.apps.permission import views

app_name = 'django_rest_template.apps.permission'

urlpatterns = [
	path(
		'venue-permission/', views.VenuePermissionListView.as_view(),
		name='venue-permission'),
]
