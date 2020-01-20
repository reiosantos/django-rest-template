from django_rest_template.apps.permission.models import VenuePermission
from django_rest_template.apps.user.constants import VIEWER_TYPE_MANAGER
from django_rest_template.apps.user.models import VenueViewerType


def make_user_venue_manager(user, venue):
	venue_manager, created = VenueViewerType.objects.get_or_create(
		venue=venue, name=VIEWER_TYPE_MANAGER)

	if created:
		venue_manager.permissions = VenuePermission.objects.all()

	venue_manager.users.add(user)
