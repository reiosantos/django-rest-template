from django.conf import settings


def site_vars(request):
	var = {
		'home_page': settings.PSP_DASHBOARD_URL,
		'media_url': settings.MEDIA_URL,
		'title': 'Django Rest Template',
		'company_name': 'Django Rest Template',
	}
	return var
