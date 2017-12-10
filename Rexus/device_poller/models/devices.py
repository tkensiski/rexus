from orator import Model
from orator.orm import belongs_to

from rexus import models


class Device(Model):

    @belongs_to
    def device_type(self):
        return models.device_types.DeviceType
