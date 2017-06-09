import logging
import sys
import time
import datetime

from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException


from rexus import logger

from rexus.config import Main as config
from rexus.devices.adc import ADC


def setup_logger():
    handler = logging.StreamHandler(stream=sys.stderr)
    formatter = logging.Formatter(fmt=config.LOG_FORMAT)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(config.LOG_LEVEL)


def main():
    setup_logger()

    while True:
        try:

            adc = ADC(config=config.devices[1])

            logger.info('Devices connected')

            while True:
                # Poll the devices
                # Spit out something so we can see whats going on
                # Eventually would be nice to send this to a nice screen with some graphs or something

                time.sleep(1)
        except Exception as e:
            try:
                logger.debug('Exception Dict: {}'.format(e.__dict__))
            except:
                pass
            logger.debug('Exception Type: {}'.format(type(e)))
            logger.debug('Exception: {}'.format(e))
            logger.info('Restarting device connection...')
            time.sleep(5)


if __name__ == '__main__':
    main()

    # While testing, lets print out the total memory used
    import os
    import psutil
    process = psutil.Process(os.getpid())

    print "\n\nMemory Used: {:0.2f} megabytes".format(process.memory_info().rss/1024.0/1024.0)
