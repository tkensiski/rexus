import logging
import random

from rexus.devices.analog_device import AnalogDevice
from rexus.config import Main as MainConfig

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class AnalogDevice(AnalogDevice):
    def __init__(self, config, interface, channel):
        super(AnalogDevice, self).__init__(
            config=config,
            interface=interface,
            min_voltage)

        if channel is None:
            raise Exception('No channel supplied, cannot read device')

        self.channel = channel
        self.voltage = None
        self.unit = 'voltage'

        # Try and get the mock voltages from the device config, otherwise just use defaults
        try:
            self.min_voltage = config['mock']['min_voltage']
            self.max_voltage = config['mock']['max_voltage']
        except:
            self.min_voltage = 1.45
            self.max_voltage = 1.60

        self.init_device()

    def init_device(self):
        self.update_voltage()

    def update_voltage(self):
        self.voltage = random.uniform(self.min_voltage, self.max_voltage)

    # Return the value that we want to display
    # Override this in the top level class
    def get_value(self):
        return self.voltage

    def __repr__(self):
        return "<AnalogDevice: {value:0.2f}{unit}> ".format(
            value=self.get_value(),
            unit=self.unit
        )
