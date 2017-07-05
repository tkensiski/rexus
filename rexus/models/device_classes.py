from orator import Model
from orator.orm import has_many

from rexus import models


class DeviceClass(Model):

    @has_many('device_class_id', 'id')
    def device_type(self):
        return models.device_types.DeviceType
