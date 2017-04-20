from __future__ import division
import time
from pprint import pprint
import datetime

from Phidgets.Devices.InterfaceKit import InterfaceKit
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException

from Display import Display
from devices.SoilMoisture import SoilMoisture

class DevicePoller():

    sbc = None

    def __init__(self):
        self.sbc = InterfaceKit()
        self.sbc.openPhidget()
        self.sbc.waitForAttach(10000)

    def read_analog_inputs(self):
        inputs = {}

        for a_input, data in self.device_map.iteritems():

            if not data:
                inputs[a_input] = False
                continue

            try:
                raw_value = self.sbc.getSensorValue(a_input)
                raw_voltage = raw_value / 200
            except PhidgetException as e:
                inputs[a_input] = e.__dict__
                continue

            if data['type'] == 'temperature_air':
                temp_c = (raw_value * 0.2222) - 61.111
                temp_f = (temp_c * 9/5) + 32

                # Our sensors can only read within this range so outside of it 
                if temp_c <= -50 or temp_c >= 150:
                    temp_c = False
                    temp_f = False

                payload = { 'c': temp_c, 'f': temp_f }

            if data['type'] == 'relative_humidity':
                payload = raw_voltage * 33.33

            if data['type'] == 'temperature_soil':
                temp_c = (raw_voltage * 41.67) -40
                temp_f = (raw_voltage * 75.006) -40

                if temp_c <= -40 or temp_c >= 85:
                    temp_c = False
                    temp_f = False

                payload = { 'c': temp_c, 'f': temp_f }

            if data['type'] == 'moisture_soil':
                sm = SoilMoisture()
                vwc = sm.find_vwc(raw_voltage)
                rvwc = sm.find_relative_vwc(vwc)
                payload = rvwc
                
            inputs[a_input] = payload

        return inputs

    def run(self):
        sleep = 1

        display = Display()

        while True:
            data = self.read_analog_inputs()

            display.write(0, "T  A Temp  RH      S Temp  S Wet")
            display.write(1, "1  {:5.2f}F  {:5.2f}%  {:5.2f}F  {:5.2f}%".format(data[0]['f'], data[2], data[4]['f'], data[6]))
            display.write(2, "2  {:5.2f}F  {:5.2f}%  {:5.2f}F  {:5.2f}%".format(data[1]['f'], data[3], data[5]['f'], data[7]))

            display.write(3, "{}".format(datetime.datetime.now().isoformat()))

            time.sleep(sleep)

        print "Done"

if __name__ == '__main__':
        dp = DevicePoller()
        dp.run()
