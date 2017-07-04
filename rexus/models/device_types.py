from orator import Model
from orator.orm import has_many, belongs_to

from rexus import models


class DeviceType(Model):

    @has_many
    def devices(self):
        return models.devices.Device

    @belongs_to
    def device_class(self):
        return models.device_classes.DeviceClass

    @has_many
    def device_formula(self):
        return models.device_formulas.DeviceFormula
