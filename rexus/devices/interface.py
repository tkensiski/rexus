from __future__ import division
import logging

from Phidgets.Devices.InterfaceKit import InterfaceKit
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException

from rexus.config import Main as MainConfig
from rexus.config import Interface as InterfaceConfig
from rexus.config import Device as DeviceConfig

from rexus.devices import InterfaceDevice

from rexus.devices.air_temperature import AirTemperature
from rexus.devices.display import Display
from rexus.devices.ph_electrode import PHElectrode
from rexus.devices.relative_humidity import RelativeHumidity
from rexus.devices.relay import Relay
from rexus.devices.soil_moisture import SoilMoisture
from rexus.devices.soil_teperature import SoilTemperature

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class Interface(InterfaceDevice):
    device_type = None
    interface = None
    config = None

    analog_input_count = None
    digital_input_count = None
    digital_output_count = None

    inputs = {
        'digital': {},
        'analog': {}
    }
    outputs = {}

    def __init__(self, config=None):
        super(Interface, self).__init__(interface=InterfaceKit(), config=config)
        super(Interface, self).connect()

        self.init_interface()

    def init_interface(self):
        self.get_counts()
        self.setup_devices()

    def get_counts(self):
        self.digital_input_count = self.interface.getInputCount()
        self.digital_output_count = self.interface.getOutputCount()
        self.analog_input_count = self.interface.getSensorCount()

    def setup_devices(self):
        self.setup_analog_devices()

    def convert_device_type_to_class_name(self, device_type=None):
        device_type = device_type.replace('_', ' ')
        device_type = device_type.title()
        device_type = device_type.replace(' ', '')

        return device_type

    def setup_analog_devices(self):
        for i in range(0, self.analog_input_count):
            device_id = self.config['inputs']['analog'].get(i)
            if device_id is not None:
                device = DeviceConfig.devices.get(device_id)
                device_type = DeviceConfig.device_types[device['type_id']]
                class_name = self.convert_device_type_to_class_name(device_type)

                module_name = 'rexus.devices.{name}'.format(name=device_type)
                module = __import__(module_name, fromlist=[class_name])
                analog_device_class = getattr(module, class_name)

                self.inputs['analog'][i] = analog_device_class(config=device, input_position=i, interface=self.interface)

    def poll_analog_devices(self):
        for i in range(0, self.analog_input_count):
            self.inputs['analog'][i].update_values()
            logger.info(self.inputs['analog'][i])




