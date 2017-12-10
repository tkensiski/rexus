import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Interface(object):

    def __init__(self, config, interface):
        if config is None:
            raise Exception('No config data for interface, cannot connect')

        logger.debug('config: {config}'.format(config=config))
        self.config = config

        self.device_type = MainConfig.device_types[config['type_id']]
        logger.info('Setting up {device_type} device'.format(device_type=self.device_type))

        if interface is None:
            raise Exception('No interface supplied, cannot connect')

        logger.debug('interface: {interface}'.format(interface=interface))
        self.interface = interface

    def setup_interface(self):
        self.channels = self._setup_channels()

    def _setup_channels(self):
        channels = {}

        device_loader = DeviceLoader()

        for channel, device_id in self.config['channels']:
            if device_id is None:
                logger.info('No device plugged into channel {channel}'.format(channel=channel))
                continue

            logger.info('Loading analog device (ID: {id}) on channel: {channel}'.format(
                id=device_id, channel=channel))

            # Fetch the device config
            device_config = MainConfig.devices.get(device_id)

            device_type = MainConfig.device_types.get(device_config.get('type_id'))
            device_class = device_loader.load_device_class(device_type=device_type)

            channels[channel] = device_class(
                config=device_config,
                interface=self,
                channel=channel
            )

        return channels
