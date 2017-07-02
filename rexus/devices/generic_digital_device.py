class DigitalDevice(Device):

    def __init__(self, config, interface):
        super(DigitalInputDevice, self).__init__(config=config, interface=interface)

        self.active = None

    # Return the value that we want to display
    # Override this in the top level class
    def get_state(self):
        return self.active

    def __repr__(self):
        return "<DigitalDevice: Active:{value}> ".format(
            value=self.get_state(),
        )
