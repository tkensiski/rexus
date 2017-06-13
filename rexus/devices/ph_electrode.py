from __future__ import division
import logging

from rexus.config import Main as MainConfig
from rexus.config import PHElectrode as PHElectrodeConfig
from rexus.devices import AnalogDevice

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class PHElectrode(AnalogDevice):
    config = None
    interface = None
    input_position = None

    raw_value = None
    raw_voltage = None

    def __init__(self, config=None, interface=None, input_position=None):
        super(PHElectrode, self).__init__(
            config=config,
            interface=interface,
            input_position=input_position
        )

        # Not implemented yet
        pass

    def __repr__(self):
        return "<PH Electrode: value: {value:0.2f}> ".format(value=self.get_value())
