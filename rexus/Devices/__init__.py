# Base Device class that all other devices extend from
from __future__ import division
import logging

from rexus.config import Device as DeviceConfig

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

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


class InterfaceDevice(Device):
    device_type = None
    interface = None
    config = None

    def __init__(self, config=None, interface=None):
        super(InterfaceDevice, self).__init__(config=config, interface=interface)
        self.config = config
        self.interface = interface

    def disconnect(self):
        logger.debug('Closing connection to device: {name}'.format(
            name=self.config.get('name')))
        self.interface.closePhidget()

    def connect(self):
        print 'Connecting'
        logger.info('Connecting to Remote Interface: {name}'.format(
            type=('Remote' if DeviceConfig.connect_remote else 'Local'),
            name=self.config.get('name')
        ))

        logger.debug(self.config)

        if DeviceConfig.connect_remote:
            self.interface.openRemote(
                serverID=self.config.get('server_id'),
                serial=self.config.get('serial_number'),
                password=self.config.get('server_password')
            )
        else:
            self.interface.OpenPhidget()

        logger.debug('Waiting {seconds} seconds for device to attach...'.format(
            seconds=(DeviceConfig.connect_timeout/1000)))
        self.interface.waitForAttach(DeviceConfig.connect_timeout)


class AnalogDevice(Device):
    device_type = None
    interface = None
    config = None
    input_position = None

    raw_value = None
    raw_voltage = None

    def __init__(self, config=None, interface=None, input_position=None):
        super(AnalogDevice, self).__init__(config=config, interface=interface)

        if input_position is None:
            raise Exception('No interface supplied, cannot create device')

        self.init_device(input_position)

    def init_device(self, input_position):
        self.config['input_position'] = input_position

        self.raw_value = self.interface.getSensorValue(input_position)
        self.raw_voltage = self.raw_value / 200

    def update_values(self):
        self.raw_value = self.interface.getSensorValue(self.config['input_position'])
        self.raw_voltage = self.raw_value / 200


    # Return the value that we want to display
    # Override this in the top level class
    def get_value(self):
        return self.raw_voltage


class DigitalDevice(Device):
    device_type = None
    interface = None

    def __init__(self, interface=None, config=None):
        super(DigitalDevice, self).__init__(config=config, interface=interface)