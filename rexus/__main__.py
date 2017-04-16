import logging
import sys

from . import logger
import config


def setup_logger():
    handler = logging.StreamHandler(stream=sys.stderr)
    formatter = logging.Formatter(fmt=config.LOG_FORMAT)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(config.LOG_LEVEL)


def main():
    setup_logger()

    


if __name__ == '__main__':
    main()

    # While testing, lets print out the total memory used so we can
    # make sure we setup lambda properly
    import os
    import psutil
    process = psutil.Process(os.getpid())

    print "\n\nMemory Used: {:0.2f} megabytes".format(process.memory_info().rss/1024.0/1024.0)
