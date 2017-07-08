import logging
import sys
import json

from rexus import database
from rexus import config as rexus_config
from rexus.models import config, devices, device_classes, device_formulas, device_types
from rexus.devices.device_loader import DeviceLoader

logger = logging.getLogger('rexus')
logger.addHandler(logging.NullHandler())


class Daemon(object):
    def __init__(self):
        # Rexus is the root of the system
        self.rexus = {}

        logger.info('Connecting to MySQL')
        database.configure_mysql()

    def load_rexus(self, types=['Raspberry Pi']):
        rexus_devices = device_types.DeviceType \
            .with_('device_class', 'devices') \
            .where_in('name', types) \
            .get()

        for rexus_device in rexus_devices:
            logger.info('Loading Rexus for device type: {type}'.format(type=rexus_device.name))
            logger.debug('Loading class {klass} from {file}'.format(
                klass=rexus_device.device_class.klass,
                type=rexus_device.name,
                file='rexus/devices/{file}.py'.format(file=rexus_device.device_class.file)
            ))

            rexus_device_class = DeviceLoader().load_device_class(
                device_type=rexus_device,
                device_class=rexus_device.device_class
            )

            # Load the devices
            for device in rexus_device.devices:
                # Thread this later
                rexus = self._load_rexus(
                    device_class=rexus_device_class,
                    device=device
                )

                if rexus is False:
                    logger.error('Unable to load rexus device {name}'.format(name=device.name))
                else:
                    logger.info('Rexus device {name} loaded successfully'.format(name=device.name))
                    self.rexus[device.id] = rexus

    def _load_rexus(self, device_class, device):
        device_config = json.loads(device.config)

        logger.info('loading root device {name} with config: {conf}'.format(
            name=device.name, conf=device_config
        ))

        rexus_device = device_class(config=device_config)
        if rexus_device.setup_interfaces() is False:
            return False

        return rexus_device


if __name__ == '__main__':
    # For local invocation
    handler = logging.StreamHandler(stream=sys.stderr)
    formatter = logging.Formatter(
        fmt=rexus_config.log_format
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(rexus_config.log_level)


    rexus = Daemon()
    rexus.load_rexus()
