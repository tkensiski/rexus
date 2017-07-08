from orator import Model
from orator.orm import has_many, has_one

from rexus import models


class DeviceType(Model):

    @has_many
    def devices(self):
        return models.devices.Device

    @has_one('id', 'device_class_id')
    def device_class(self):
        return models.device_classes.DeviceClass

    @has_many('device_type_id', 'id')
    def device_formulas(self):
        return models.device_formulas.DeviceFormula
