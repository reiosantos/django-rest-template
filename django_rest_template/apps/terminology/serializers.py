from rest_framework import serializers

from django_rest_template.apps.terminology.models import Translation


class TranslationSerializer(serializers.ModelSerializer):
	term = serializers.CharField()

	language = serializers.CharField()

	class Meta:
		model = Translation
		fields = (
			'term',
			'language',
			'value',
		)
