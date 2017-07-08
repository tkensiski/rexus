from __future__ import division
import logging
import json

from ..models import config, devices, device_classes, device_formulas, device_types
from rexus import Rexus
from device_loader import DeviceLoader

# These are imported by setup_devices
# from rexus.devices.{DeviceType} import {DeviceType}

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class RaspberryPi(Rexus):
    def __init__(self, config):
        super(RaspberryPi, self).__init__(config=config)
        logger.debug('Initializing RaspberryPi')

    def setup_interfaces(self):
        # Loop the adc_ids (device ids)
        for ID in self.config['interface_ids']:
            interface = devices.Device \
                .with_('device_type', 'device_type.device_class') \
                .where('id', ID) \
                .first()

            device_klass = interface.device_type.device_class

            logger.info('Loading device class for {type}'.format(type=interface.name))
            logger.debug('Loading class {klass} from {file}'.format(
                klass=device_klass.klass,
                type=interface.device_type.name,
                file='rexus/devices/{file}.py'.format(file=device_klass.file)
            ))

            device_class = DeviceLoader().load_device_class(
                device_type=interface.device_type,
                device_class=device_klass
            )

            # Setup the interface!
            interface_device = self._load_interface(
                device_class=device_class,
                device=interface
            )

            if interface_device is False:
                logger.error('Unable to load interface device {name}'.format(name=interface.name))
            else:
                logger.info('{name} loaded successfully'.format(name=interface.name))
                self.interfaces[interface.id] = interface_device

    def _load_interface(self, device_class, device):
        device_config = json.loads(device.config)

        if self.is_conflicting_bus(interface_config['address']) is True:
            logger.error('Bus ID is in conflict for this device. Resolve this conflict to load')
            return False

        logger.info('loading interface device {name} with config: {conf}'.format(
            name=device.name, conf=device_config
        ))

        interface = device_class(config=device_config)
        if interface.setup_interface() is False:
            return False

        return interface
