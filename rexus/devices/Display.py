import logging

from Phidgets.Devices.TextLCD import TextLCD, TextLCD_ScreenSize
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException

from rexus.config import Main as MainConfig
from rexus.config import Display as DisplayConfig
from rexus.devices import InterfaceDevice

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class Display(InterfaceDevice):

    interface = None
    config = None

    row_count = None
    column_count = None

    def __init__(self, config=None):
        super(Display, self).__init__(interface=TextLCD(), config=config)
        super(Display, self).connect()

        self.init_interface()
        self.clear_screen()

    def init_interface(self):
        # Configure the display
        self.interface.setBacklight(DisplayConfig.BACKLIGHT)
        self.interface.setContrast(DisplayConfig.CONTRAST)
        self.interface.setScreenSize(DisplayConfig.SIZE)
        self.interface.setScreenIndex(0)

        self.row_count = self.interface.getRowCount()
        self.column_count = self.interface.getColumnCount()

    def clear_screen(self):
        for row in range(0, self.row_count):
            self.write(row, "")

    def write(self, row, text):
        try:
            self.interface.setDisplayString(row, text)
        except PhidgetException as e:
            logger.error(e.__dict__)
