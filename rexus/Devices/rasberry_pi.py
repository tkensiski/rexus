from __future__ import division
import logging

from rexus.config import Main as MainConfig

from rexus.devices import DeviceLoader
from rexus.devices.adc import ADC

# These are imported by setup_devices
# from rexus.devices.{DeviceType} import {DeviceType}

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class RasberryPi(object):

    interfaces = {
    ''' adc_device_id: {
            adc: <ADC>,
            devices: {
                channel_id: device,
                ...
            }
        },
    '''
    }

    def __init__(self, config=None):
        super(RasberryPi, self).__init__(config=config)

        self.init_interface()

    def init_interface(self):
        self.setup_adcs()

    def setup_adcs(self):
        # Loop the adc_ids (device ids)
        for interface_device_id in self.config.interface_ids:
            interface_config = MainConfig.devices.get(interface_device_id, None)
            bus_id = interface_config.get('address', 76)

            if bus_id in I2C_bus:
                device_name = interface_config.get('name')
                raise Exception('The I2C bus conflict for device {device_name} using address '
                    '{address}, resolve conflict to use this device.'.format(
                        device_name=device_name, address=interface_config.get('address')
                    ))

            device_type = MainConfig.device_types.get(interface_config.get('type_id'))
            device_class = device_loader.load_device_class(device_type=device_type)

            # Setup the ADC!
            self.adcs[interface_device_id] = {
                'interface': device_class(config=interface_config),
                'devices': {
                    # Channel ID: Device, ...
                }
            }

            self.setup_devices(self, adc_id=interface_device_id, config=interface_config)

    def setup_devices(self, adc_id=None, config=None):
        for channel_id, device_id in config.get('channels')
            device_config = MainConfig.devices.get(device_id, None)

            device_type = MainConfig.device_types.get(device_config.get('type_id'))
            device_class = device_loader.load_device_class(device_type=device_type)

            self.interfacesI2C_bus[bus_id] = device_class(
                config=device_config,
            )
