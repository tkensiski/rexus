from __future__ import division
import logging

from rexus.config import Main as MainConfig
from rexus.config import SoilMoisture as SoilMoistureConfig
from rexus.devices import AnalogDevice

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class SoilMoisture(AnalogDevice):
    config = None
    interface = None
    input_position = None

    raw_value = None
    raw_voltage = None

    vwc = None
    rvwc = None

    def __init__(self, config=None, interface=None, input_position=None):
        super(SoilMoisture, self).__init__(
            config=config,
            interface=interface,
            input_position=input_position
        )

    def find_slope(self, pointA, pointB):
        rise = float(pointB.x) - float(pointA.x)
        run = float(pointB.y) - float(pointA.y)
        slope = rise/run

        return slope

    def find_closest_voltages(self, voltage, soil_moisture=SoilMoistureConfig.soil_moisture):
        point1 = min(soil_moisture.values(), key=lambda x:abs(x-voltage))
        soil_moisture = dict(soil_moisture)
        del soil_moisture[SoilMoistureConfig.soil_moisture_by_voltage[str(point1)]]
        point2 = min(soil_moisture.values(), key=lambda x:abs(x-voltage))

        return (point1, point2)

    def find_vwc(self, voltage):
        if voltage <= SoilMoistureConfig.soil_moisture[0]:
            return 0

        v1, v2 = self.find_closest_voltages(voltage)
        point1 = Point(vwc=SoilMoistureConfig.soil_moisture_by_voltage[str(v1)], voltage=v1)
        point2 = Point(vwc=SoilMoistureConfig.soil_moisture_by_voltage[str(v2)], voltage=v2)
        m = self.find_slope(point1, point2)

        vwc = m * (voltage - point1.y) + point1.x

        if vwc > 100:
            vwc = 100

        return vwc

    def find_relative_vwc(self, vwc):
        if vwc <= 0:
            return 0

        if vwc >= 55:
            return 100

        rw = 100 * ( vwc / 55 )

        return rw

    # Return the value that we want to display
    def get_value(self):
        self.vwc = self.find_vwc(self.raw_voltage)
        self.rvwc = self.find_relative_vwc(self.vwc)
        return self.rvwc

    def __repr__(self):
        return "<SoilMoisture: RVWC: {value:0.2f}%> ".format(value=self.get_value())


class Point:
    def __init__ (self, vwc, voltage):
        self.x = vwc
        self.y = voltage


if __name__ == '__main__':
    import random

    for i in range(0,10):
        voltage = random.uniform(0.00,3.00)

        voltage = float(voltage)

        sm = SoilMoisture()
        vwc = sm.find_vwc(voltage)
        rvwc = sm.find_relative_vwc(vwc)

        print "Voltage: {volt:0.2f} is VWC: {vwc:0.2f}; Relative VWC: {rvwc:0.2f}".format(
            volt = voltage, vwc=vwc, rvwc=rvwc )