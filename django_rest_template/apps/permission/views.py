from rest_framework.generics import ListAPIView

from django_rest_template.apps.permission.models import VenuePermission
from django_rest_template.apps.permission.permissions import ManagementPermissions
from django_rest_template.apps.permission.serializers import VenuePermissionSerializer


class VenuePermissionListView(ListAPIView):
	serializer_class = VenuePermissionSerializer
	permission_classes = (ManagementPermissions,)
	queryset = VenuePermission.objects.all()
