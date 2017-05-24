from __future__ import division
import logging

#from Phidgets.Devices.InterfaceKit import InterfaceKit
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException

from rexus.config import Main as MainConfig
from rexus.config import RelativeHumidity as RelativeHumidityConfig
from rexus.devices import AnalogDevice

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class RelativeHumidity(AnalogDevice):
    config = None
    interface = None
    input_position = None

    raw_value = None
    raw_voltage = None

    rh = None

    def __init__(self, config=None, interface=None, input_position=None):
        super(RelativeHumidity, self).__init__(
            config=config,
            interface=interface,
            input_position=input_position
        )

    def find_rh(self, raw_voltage=None):
        return raw_voltage * 33.33

    # Return the value that we want to display
    def get_value(self):
        self.rh = self.find_rh(self.raw_voltage)
        return self.rh

    def __repr__(self):
        return "<RelativeHumidity: RH: {value:0.2f}%> ".format(value=self.get_value())



