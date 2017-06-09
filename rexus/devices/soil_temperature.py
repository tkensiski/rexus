from __future__ import division
import logging

#from Phidgets.Devices.InterfaceKit import InterfaceKit
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException

from rexus.config import Main as MainConfig
from rexus.config import SoilTemperature as SoilTemperatureConfig
from rexus.devices import AnalogDevice

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

"""
This SoilTemperature class supports the THERM200 from vegetronix
https://www.vegetronix.com/Products/THERM200/
"""

class SoilTemperature(AnalogDevice):
    config = None
    interface = None
    input_position = None

    raw_value = None
    raw_voltage = None

    temp = { 'F': None, 'C': None }

    def __init__(self, config=None, interface=None, input_position=None):
        super(SoilTemperature, self).__init__(
            config=config,
            interface=interface,
            input_position=input_position
        )

    def getMetricValue(self, raw_value=None):
        return (raw_value * 41.67) -40

    def getImperialValue(self, raw_value=None):
        return (raw_value * 75.006) -40

    # Return the value that we want to display
    def get_value(self):
        self.temp['C'] = self.getMetricValue(raw_value=self.raw_value)
        self.temp['F'] = self.getImperialValue(raw_value=self.raw_value)

        return self.temp['C'] if MainConfig.display_units == 'metric' else self.temp['F']

    def __repr__(self):
        unit = 'C' if MainConfig.display_units == 'metric' else 'F'

        return "<SoilTemperature: Temp: {value:0.2f}{unit}> ".format(
            value=self.get_value(),
            unit=unit
        )
