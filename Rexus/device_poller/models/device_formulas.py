from orator import Model
from orator.orm import has_one

from rexus import models


class DeviceFormula(Model):

    @has_one('id', 'device_type_id')
    def device_type(self):
        return models.device_types.DeviceType
