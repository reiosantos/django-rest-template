from rest_framework import serializers

from django_rest_template.apps.permission.models import VenuePermission


class VenuePermissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = VenuePermission
		fields = ('permission_name',)
