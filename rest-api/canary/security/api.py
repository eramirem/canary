from tastypie.resources import ModelResource
from tastypie import fields
from security.models import *
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class SystemResource(ModelResource):
	class Meta:
		queryset = System.objects.all()
		resource_name = 'systems'
		authorization = Authorization()
		filtering = {
			"status" : ALL,
		}

class SensorResource(ModelResource):
	system = fields.ForeignKey(SystemResource, 'system', full=True)

	class Meta:
		queryset = Sensor.objects.all()
		resource_name = 'sensors'
		authorization = Authorization()
		filtering = {
			"system" : ALL,
			"name" : ALL,
		}