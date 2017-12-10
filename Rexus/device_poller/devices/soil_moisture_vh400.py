from __future__ import division
import logging

from rexus.devices.analog_device import AnalogDevice

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class SoilMoisture(AnalogDevice):
    """
    This SoilMoisture class supports the VH400 from vegetronix
    https://www.vegetronix.com/Products/VH400/

    Why this sensor over other cheaper ones:
    'Because our probe measures the dielectric constant of the soil using
    transmission line techniques, it is insensitive to water salinity, and will
    not corrode over time as does conductivity based probes. Our probes are
    small, rugged, and low power.' - vegetronix
    """


    # VWC to Voltage of the sensor
    # Number of points will dictate the Human readable % so that way after a
    # watering it will read 100% for a period of time
    # How To Get Datapoints: http://www.vegetronix.com/TechInfo/How-To-Measure-VWC.phtml
    soil_moisture = {
        # Volumetric Water Content (vwc): Sensor Voltage (v)
        # x : y
        0: 0.26,
        5: 0.65,
        10: 1.05,
        15: 1.25,
        20: 1.64,
        25: 1.85,
        30: 2.00,
        35: 2.10,
        40: 2.38,
        45: 2.50,
        50: 2.60,
        55: 2.92
    }

    soil_moisture_by_voltage = {}

    def __init__(self, config=None, interface=None, input_position=None):
        super(SoilMoisture, self).__init__(
            config=config,
            interface=interface,
            input_position=input_position
        )

        raw_value = None
        raw_voltage = None

        vwc = None
        rvwc = None

        for key, value in self.soil_moisture.iteritems():
            self.soil_moisture_by_voltage[str(value)] = key

    def find_slope(self, pointA, pointB):
        rise = float(pointB.x) - float(pointA.x)
        run = float(pointB.y) - float(pointA.y)
        slope = rise/run

        return slope

    def find_closest_voltages(self, voltage):
        # Make a dupe so we dont modify the real dict
        soil_moisture = dict(self.soil_moisture)

        v1 = min(soil_moisture.values(), key=lambda x: abs(x-voltage))
        del soil_moisture[self.soil_moisture_by_voltage[str(v1)]]
        v2 = min(soil_moisture.values(), key=lambda x: abs(x-voltage))

        return (v1, v2)

    def find_vwc(self, voltage):
        if voltage <= self.soil_moisture[0]:
            return 0

        v1, v2 = self.find_closest_voltages(voltage=voltage)
        vwc1 = self.soil_moisture_by_voltage[str(v1)]
        vwc2 = self.soil_moisture_by_voltage[str(v2)]
        point1 = Point(vwc=vwc1, voltage=v1)
        point2 = Point(vwc=vwc2, voltage=v2)
        m = self.find_slope(point1, point2)

        real_vwc = m * (voltage - point1.y) + point1.x

        if real_vwc > 100:
            real_vwc = 100

        return real_vwc

    def find_relative_vwc(self, vwc):
        if vwc <= 0:
            return 0

        if vwc >= 55:
            return 100

        rvwc = 100 * (vwc / 55)

        return rvwc

    # Return the value that we want to display
    def get_value(self):
        self.vwc = self.find_vwc(self.raw_voltage)
        self.rvwc = self.find_relative_vwc(self.vwc)
        return self.rvwc

    def __repr__(self):
        return "<SoilMoisture: RVWC: {value:0.2f}%> ".format(value=self.get_value())


class Point:
    def __init__(self, vwc, voltage):
        self.x = vwc
        self.y = voltage
