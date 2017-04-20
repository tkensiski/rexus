import time
from pprint import pprint

from Phidgets.Devices.TextLCD import TextLCD, TextLCD_ScreenSize
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException

class Display():

    display = None

    BACKLIGHT = True
    CONTRAST = 180
    SIZE = TextLCD_ScreenSize.PHIDGET_TEXTLCD_SCREEN_4x40

    def __init__(self):
        self.connect()
        self.setup()
        self.clear_screen()

    def connect(self):
        self.display = TextLCD()
        self.display.openPhidget()
        self.display.waitForAttach(10000)

    def setup(self):
        # Configure the display
        self.display.setBacklight(self.BACKLIGHT)
        self.display.setContrast(self.CONTRAST)
        self.display.setScreenSize(self.SIZE)
        self.display.setScreenIndex(0)

    def clear_screen(self):
        for row in range(0,self.display.getRowCount()):
            self.write(row, "")

    def write(self, row, text):
        try:
            self.display.setDisplayString(row, text)
        except PhidgetException as e:
            print e.__dict__
        #time.sleep(1)

if __name__ == '__main__':
        display = Display()
        display.write(1, 'Testing a new message for kaser')
