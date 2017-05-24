import logging
import sys
import time
import datetime

from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException


from rexus import logger

from rexus.config import Main as config
from rexus.config import Device as DeviceConfig
from rexus.devices.interface import Interface
from rexus.devices.display import Display


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
            sbc = Interface(config=DeviceConfig.devices[0])
            display = Display(config=DeviceConfig.devices[16])

            logger.info('Devices connected')

            while True:
                sbc.poll_analog_devices()
                display.write(0, "T  A Temp  RH      S Temp  S Wet")    

                display.write(1, "R  {air_temp:5.2f}F  {relative_humidity:5.2f}%  {soiL_temp:5.2f}F  {soil_moisture:5.2f}%".format(
                    air_temp=sbc.inputs['analog'][0].get_value(),
                    relative_humidity=sbc.inputs['analog'][3].get_value(),
                    soiL_temp=0,
                    soil_moisture=sbc.inputs['analog'][1].get_value()
                ))

                display.write(2, "L  {air_temp:5.2f}F  {relative_humidity:5.2f}%  {soiL_temp:5.2f}F  {soil_moisture:5.2f}%".format(
                    air_temp=sbc.inputs['analog'][4].get_value(),
                    relative_humidity=sbc.inputs['analog'][7].get_value(),
                    soiL_temp=0,
                    soil_moisture=sbc.inputs['analog'][5].get_value()
                ))

                display.write(3, "{}".format(datetime.datetime.now().isoformat()))

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

    # While testing, lets print out the total memory used so we can
    # make sure we setup lambda properly
    import os
    import psutil
    process = psutil.Process(os.getpid())

    print "\n\nMemory Used: {:0.2f} megabytes".format(process.memory_info().rss/1024.0/1024.0)
