from __future__ import division
import logging
from smbus import SMBus
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

    # for older PI's (version 1)
    pi_version_1 = False

    # Determine the reference voltage
    voltage_reference = 5

    # To calculate the voltage, the number read in is 3 bytes. The first bit is ignored.
    # Max reading is 2^23 or 8,388,608
    max_reading = 8388608.0

    # lange = number of bytes to read. A minimum of 3 bytes are read in.
    # In this sample we read in 6 bytes,
    # ignoring the last 3 bytes. number of bytes to read in the block
    lange = 0x06

    # zeit (German for time) - tells how frequently you want the readings to be read from the ADC.
    # Define the time to sleep between the readings.
    # Number of seconds to sleep between each measurement
    zeit = 5

    # sleep shows how frequently each channel is read in over the I2C bus. Best to use sleep
    # between each successive readings. number of seconds to sleep between each channel reading
    # has to be more than 0.2 (seconds).
    sleep = 0.5

    # address is the address of the ADC chip.
    # Use i2cdetect -y 1 to find the address. Use "y 0" for older Pi's.
    #
    # Depending on the jumper settings A0, A1 and A2, all possible combinations are shown below.
    # Please refer to LTC 2495 data sheet, available at wwww.linear.com
    # Page 17 of the data sheet has this information.
    # Also see the Pi-16ADC User Guide for more information.
    #
    # The address - 0x76 is the default address for Pi-16ADC.
    addresses = {
        #   ADDRESS       A2    A1     A0
        14: 0b0010100,  # LOW   LOW    LOW     0x14
        16: 0b0010110,  # LOW   LOW    HIGH    0x16
        15: 0b0010101,  # LOW   LOW    FLOAT   0x15
        26: 0b0100110,  # LOW   HIGH   LOW     0x26
        34: 0b0110100,  # LOW   HIGH   HIGH    0x34
        27: 0b0100111,  # LOW   HIGH   FLOAT   0x27
        17: 0b0010111,  # LOW   FLOAT  LOW     0x17 # Default
        25: 0b0100101,  # LOW   FLOAT  HIGH    0x25
        24: 0b0100100,  # LOW   FLOAT  FLOAT   0x24
        56: 0b1010110,  # HIGH  LOW    LOW     0x56
        64: 0b1100100,  # HIGH  LOW    HIGH    0x64
        57: 0b1010111,  # HIGH  LOW    FLOAT   0x57
        74: 0b1110100,  # HIGH  HIGH   LOW     0x74
        76: 0b1110110,  # HIGH  HIGH   HIGH    0x76
        75: 0b1110101,  # HIGH  HIGH   FLOAT   0x75
        65: 0b1100101,  # HIGH  FLOAT  LOW     0x65
        67: 0b1100111,  # HIGH  FLOAT  HIGH    0x67
        66: 0b1100110,  # HIGH  FLOAT  FLOAT   0x66
        35: 0b0110101,  # FLOAT LOW   LOW      0x35
        37: 0b0110111,  # FLOAT LOW   HIGH     0x37
        36: 0b0110110,  # FLOAT LOW   FLOAT    0x36
        47: 0b1000111,  # FLOAT HIGH  LOW      0x47
        55: 0b1010101,  # FLOAT HIGH  HIGH     0x55
        54: 0b1010100,  # FLOAT HIGH  FLOAT    0x54
        44: 0b1000100,  # FLOAT FLOAT LOW      0x44
        46: 0b1000110,  # FLOAT FLOAT HIGH     0x46
        45: 0b1000101,  # FLOAT FLOAT FLOAT    0x45
    }

    # Channel Address - Single channel use
    # See LTC2497 data sheet, Table 3, Channel Selection.
    # All channels are uncommented - comment out the channels you do not plan to use.
    channels = {
        0: 0xB0,
        1: 0xB8,
        2: 0xB1,
        3: 0xB9,
        4: 0xB2,
        5: 0xBA,
        6: 0xB3,
        7: 0xBB,
        8: 0xB4,
        9: 0xBC,
        10: 0xB5,
        11: 0xBD,
        12: 0xB6,
        13: 0xBE,
        14: 0xB7,
        15: 0xBF,
    }

    def __init__(self, config=None):
        # for older PI's (version 1) use bus 0 instead of 1
        bus = 1 if self.pi_version_1 is False else 0
        super(ADC, self).__init__(self, config=config, interface=SMBus(bus))
        time.sleep(self.tiempo)

        # Set the address
        self.address = self.config.get('address', 76)

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
