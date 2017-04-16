from __future__ import division
from rexus import config

class SoilMoisture:

    def find_slope(self, pointA, pointB):
        rise = float(pointB.x) - float(pointA.x)
        run = float(pointB.y) - float(pointA.y)
        slope = rise/run

        return slope

    def find_closest_voltages(self, voltage, soil_moisture=config.soil_moisture):

        point1 = min(soil_moisture.values(), key=lambda x:abs(x-voltage))
        soil_moisture = dict(soil_moisture)
        del soil_moisture[config.soil_moisture_by_voltage[str(point1)]]
        point2 = min(soil_moisture.values(), key=lambda x:abs(x-voltage))

        return (point1, point2)

    def lookup_vwc_from_voltage(self, voltage):
        return config.soil_moisture.keys()[config.soil_moisture.values().index(voltage)]

    def find_vwc(self, voltage):
        if voltage <= config.soil_moisture[0]:
            return 0

        v1, v2 = self.find_closest_voltages(voltage)
        point1 = Point(vwc=config.soil_moisture_by_voltage[str(v1)], voltage=v1)
        point2 = Point(vwc=config.soil_moisture_by_voltage[str(v2)], voltage=v2)
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


class Point:
    def __init__ (self, vwc, voltage):
        self.x = vwc
        self.y = voltage
        

if __name__ == '__main__':

    import sys
    voltage = float(sys.argv[1] if sys.argv[1] else 0)

    sm = SoilMoisture()
    vwc = sm.find_vwc(voltage)
    rvwc = sm.find_relative_vwc(vwc)

    print "Voltage: {volt:0.2f} is VWC: {vwc:0.2f}; Relative VWC: {rvwc:0.2f}".format(
        volt = voltage, vwc=vwc, rvwc=rvwc )