from django.contrib import admin

from django_rest_template.apps.oauth.models import (OAuthProvider, VenueToken)

admin.site.register(OAuthProvider)
admin.site.register(VenueToken)
