from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from django_rest_template.apps.user import views

app_name = 'django_rest_template.apps.user'

router = DefaultRouter()
router.register('organisation', views.UsersInOrganisationViewSet, basename='in-organisation', )
router.register('viewer-types', views.VenueViewerTypesViewSet, basename='viewer-types', )
router.register('short/organisation', views.UsersInOrganisationShortViewSet,
                basename='in-organisation-short', )


urlpatterns = [
	path('current/', views.CurrentUserView.as_view(), name='current'),
	path('update/', views.EditProfileView.as_view(), name='edit'),
	path('activate/', views.ActivateUserView.as_view(), name='activate'),
	path('signup/', views.CreateUserView.as_view(), name='signup'),
	path('dashboard-sections/', views.DashboardSectionsView.as_view(), name='dashboard-sections'),
	path('venue-permissions/', views.UserVenuePermissionsView.as_view(), name='dashboard-sections'),
	path('verify-exists/', views.UserExistView.as_view(), name='verify-user'),
	path('', include(router.urls))
]
