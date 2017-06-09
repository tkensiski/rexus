from __future__ import division
import logging

from rexus.config import Main as MainConfig
from rexus.config import AirTemperature as AirTemperatureConfig
from rexus.devices import AnalogDevice

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

"""
Supports: http://www.phidgets.com/products.php?category=35&product_id=1124_0
"""

class AirTemperature(AnalogDevice):
    config = None
    interface = None
    input_position = None

    raw_value = None
    raw_voltage = None

    temp = { 'F': None, 'C': None }

    def __init__(self, config=None, interface=None, input_position=None):
        super(AirTemperature, self).__init__(
            config=config,
            interface=interface,
            input_position=input_position
        )

    def getMetricValue(self, raw_value=None):
        return (raw_value * 200 * 0.2222) - 61.111

    def getImperialValue(self, metric_value=None):
        return (metric_value * 9/5) + 32

    # Return the value that we want to display
    def get_value(self):
        self.temp['C'] = self.getMetricValue(raw_value=self.raw_value)
        self.temp['F'] = self.getImperialValue(metric_value=self.temp['C'])

        return self.temp['C'] if MainConfig.display_units == 'metric' else self.temp['F']

    def __repr__(self):
        unit = 'C' if MainConfig.display_units == 'metric' else 'F'

        return "<AirTemperature: Temp: {value:0.2f}{unit}> ".format(
            value=self.get_value(),
            unit=unit
        )
