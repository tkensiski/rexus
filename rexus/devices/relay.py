from __future__ import division
import logging

from rexus.config import Main as MainConfig
from rexus.config import Relay as RelayConfig

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class Relay():

    config = None
    device = None

    def __init__(self, config=None):

        if not config:
            raise Exception('No config data for Relay')

        # Not implemented yet
        pass


