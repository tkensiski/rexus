from __future__ import division
import logging
import time

from rexus.devices import Interface

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


"""
Initially built for Alchamy Powers 16 input ADC
http://alchemy-power.com/pi-16adc/

Should support any ADC that uses the SMBus reader
"""
class ADC(Interface):

    def __init__(self, config=None):
        # for older PI's (version 1) use bus 0 instead of 1
        super(ADC, self).__init__(self, config=config, interface=Interface)

    def read_channel(self, channel=None):
        # Translate the address and channels into their hex representations
        hex_address = self.addresses.get(self.address, None)
        hex_channel = self.channels.get(channel, None)

        if hex_address is None or hex_channel is None:
            raise Exception('Must specify address and channel to read data from the device')

        self.logger.info('Reading data from channel {channel} on ADC {address}'.format(
            channel=channel, address=self.address))

        self.interface.write_byte(hex_address, hex_channel)

        # Give the device a second to do something...
        time.sleep(self.tiempo)

        reading = self.interface.read_i2c_block_data(hex_address, hex_channel, 0x06)
        logger.debug('Channel {channel} reading: {reading}'.format(
            channel=channel, reading=reading
        ))

        # Not really sure how this comparison stuff and math below works...
        # At some point id like to understand but for now I know its using bitwise operators...
        # https://wiki.python.org/moin/BitwiseOperators
        # Convert the channel reading into a value
        value = ((((reading[0] & 0x3F)) << 16)) + ((reading[1] << 8)) + (((reading[2] & 0xE0)))

        # See if we are out of bounds after we get the value so the log means something useful
        if (reading[0] & 0b11000000) == 0b11000000:
            self.debug(
                ('Input voltage to channel {channel} is either open or more than {vref:1.2f}.'
                 ' Value read: {value} volts').format(
                    channel=channel,
                    vref=self.vref,
                    value=value
                )
            )

        # Convert the value to a voltage
        volts = value * self.vref / self.max_reading
        logger.debug('Channel {channel} voltage: {voltage:1.2f}'.format(
            channel=channel, voltage=volts))

        return volts
