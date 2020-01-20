from django.urls import path, re_path

from django_rest_template.apps.venue import views

app_name = 'django_rest_template.apps.venue'

urlpatterns = [
	path('settings/', views.VenueSettingsView.as_view(), name="settings"),
	path('venues/', views.VenuesListView.as_view(), name="list-all-venues"),
	re_path(r'settings/(?P<path>[\w-]+)/', views.VenueSettingsUpdateView.as_view(), name="setting"),
	path('countries/', views.CountriesView.as_view(), name='countries'),
	re_path(r'countries/(?P<country>[A-Z]{2})/', views.ListVenuesView.as_view(), name='for-country')
]
