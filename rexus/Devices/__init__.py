# Base Device class that all other devices extend from
from __future__ import division
import logging

from rexus.config import Device as DeviceConfig

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class DeviceLoader(object):
    device_classes = {
        # class_name : getattr(module, class_name)
    }

    def load_device_class(self, device_type=None):
        logger.info('Loading class for device type: {device_type}'.format(device_type=device_type))

        if device_type in self.device_classes:
            logger.debug('Class already loaded for device type: {device_type}'.format(
                device_type=device_type))
            return self.device_classes.get(device_type)

        return _load_device_class(device_type=device_type)

    def _convert_device_type_to_class_name(self, device_type=None):
        device_type = device_type.replace('_', ' ')
        device_type = device_type.title()
        device_type = device_type.replace(' ', '')

        return device_type

    def _load_device_class(self, device_type=None):
        class_name = self._convert_device_type_to_class_name(device_type)

        module_name = 'rexus.devices.{name}'.format(name=device_type)
        module = __import__(module_name, fromlist=[class_name])
        device_class = getattr(module, class_name)

        self._memoize_device_class(device_type=device_type, device_class=device_class)

        return device_class

    def _memoize_device_class(self, device_type=None, device_class=None):
        if device_type in self.device_classes:
            return True, self.device_classes.get(device_type)

        self.device_classes[class_name] = device_class


class Interface(object):
    interface = None
    config = {}
    channels = {}

    def __init__(self, config=None, interface=None):

        if interface is None:
            raise Exception('No interface supplied, cannot connect')

        logger.debug('interface: {interface}'.format(interface=interface))
        self.interface = interface

        self.channels = self.setup_channels()

    def setup_channels(self):
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

            device_type = DeviceConfig.device_types.get(device_config.get('type_id'))
            device_class = device_loader.load_device_class(device_type=device_type)

            channels[i] = device_class(
                config=device_config,
                interface=self,
                channel=channel
            )

        return channels

    def poll_all_channels(self):
        for channel_id, device in self.channels.iteritems():
            device.update_voltage()


class Device(object):
    device_type = None
    interface = None
    config = None

    def __init__(self, config=None, interface=None):
        self.device_type = DeviceConfig.device_types[config['type_id']]
        logger.info('Setting up {device_type} device'.format(device_type=self.device_type))

        if config is None:
            raise Exception('No config data for interface, cannot connect')

        logger.debug('config: {config}'.format(config=config))
        self.config = config

        if interface is None:
            raise Exception('No interface supplied, cannot create device')

        logger.debug('interface: {interface}'.format(interface=interface))
        self.interface = interface


class AnalogDevice(Device):
    channel = None
    voltage = None

    def __init__(self, config=None, interface=None, channel=None):
        super(AnalogDevice, self).__init__(config=config, interface=interface)

        if channel is None:
            raise Exception('No channel supplied, cannot read device')

        self.channel = channel

        self.init_device()

    def init_device(self):
        self.update_voltage()

    def update_voltage(self):
        self.voltage = self.interface.read_channel(channel=self.channel)

    # Return the value that we want to display
    # Override this in the top level class
    def get_value(self):
        return self.voltage

    def __repr__(self):
        unit = 'voltage'
        return "<AnalogDevice: {value:0.2f}{unit}> ".format(
            value=self.get_value(),
            unit=unit
        )


class DigitalDevice(Device):
    active = None

    def __init__(self, config=None, interface=None):
        super(DigitalInputDevice, self).__init__(config=config, interface=interface)

        self.active = None

    # Return the value that we want to display
    # Override this in the top level class
    def get_state(self):
        return self.active

    def __repr__(self):
        return "<DigitalDevice: Active:{value}> ".format(
            value=self.get_state(),
        )

