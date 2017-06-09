from __future__ import division
import logging

#from Phidgets.Devices.InterfaceKit import InterfaceKit
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException

from rexus.config import Main as MainConfig
from rexus.config import RelativeHumidity as RelativeHumidityConfig
from rexus.devices import AnalogDevice

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


"""
This RelativeHumidity class supports the VG-HUMID from vegetronix
https://www.vegetronix.com/Products/VG-HUMID/

Why this sensor over other cheaper ones:
'The sensor and electronics are enclosed in a weather resistant flanged box for easy
mounting. The electronic sensor is directly connected to the outside air through a
small inlet tube, on the bottom side of the box near the cable gland. Because the small
inlet tube isolates the sensor from the rest of the air volume in the box, latency
to changes in relative air humidity is reduced.'
"""

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



