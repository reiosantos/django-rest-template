from rest_framework.renderers import JSONRenderer

from django_rest_template.apps.common.psp_camel_case.util import camelize


class CamelCaseJSONRenderer(JSONRenderer):
	def render(self, data, *args, **kwargs):
		return super(CamelCaseJSONRenderer, self).render(camelize(data), *args, **kwargs)
