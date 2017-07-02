from __future__ import division
import logging

from rexus.config import Main as MainConfig

from rexus.devices import DeviceLoader
from rexus.devices.adc import ADC

# These are imported by setup_devices
# from rexus.devices.{DeviceType} import {DeviceType}

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class RaspberryPi(object):

    # Make sure we keep track of what bus addresses that we init
    # so we dont init double and rather alert that theres a duplicate
    # address in use
    bus_addresses = []

    interfaces = {
        # interface_id: <DeviceType (Interface)>,
    }

    def __init__(self, config):
        self.config = config
        self.interfaces = {}
        self.setup_interfaces()
        self.setup_devices()

    def setup_interfaces(self):
        # Loop the adc_ids (device ids)
        for ID in self.config.interface_ids:
            interface_config = MainConfig.devices.get(ID)
            bus_id = interface_config.get('address')
            interface_name = interface_config.get('name')

            if bus_id in self.bus_addresses:
                raise Exception('The I2C bus conflict for device {device_name} using address '
                    '{address}, resolve conflict to use this device.'.format(
                        device_name=interface_name,
                        address=interface_config.get('address')
                    ))

            interface_type_id = interface_config.get('type_id')
            device_type = MainConfig.device_types.get(interface_type_id)
            device_class = device_loader.load_device_class(device_type=device_type)

            # Setup the interface!
            self.interfaces[ID] = device_class(config=interface_config)

            # Now its channels
            try:
                self.interfaces[ID].setup_channels(adc_id=ID, config=interface_config)
            except Exception as e:
                logger.error('Something went wrong when setting up channels on '
                     'the {name} interface: {error}'.format(name=interface_name, error=e))
