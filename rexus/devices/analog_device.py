import logging

from rexus.devices import Device
from rexus.config import Main as MainConfig

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class AnalogDevice(Device):

    def __init__(self, config, interface, channel):
        super(AnalogDevice, self).__init__(config=config, interface=interface)

        if channel is None:
            raise Exception('No channel supplied, cannot read device')

        self.channel = channel
        self.voltage = None
        self.unit = 'voltage'

        self.init_device()

    def init_device(self):
        self.update_voltage()

    def update_voltage(self):
        self.voltage = self.interface.read_channel(channel=self.channel)

    # Return the value that we want to display
    # Override this in the top level class
    def get_value(self):
        return self.voltage

    def __repr__(self):
        return "<AnalogDevice: {value:0.2f}{unit}> ".format(
            value=self.get_value(),
            unit=self.unit
        )
