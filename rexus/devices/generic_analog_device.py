class AnalogDevice(Device):

    def __init__(self, config, interface, channel):
        super(AnalogDevice, self).__init__(config=config, interface=interface)

        if channel is None:
            raise Exception('No channel supplied, cannot read device')

        self.channel = channel
        self.voltage = None

        self.init_device()

    def init_device(self):
        self.update_voltage()

    def update_voltage(self):
        # Check to see if we are in mock mode where we send mock voltages back
        if MainConfig.mock_channels is False:
            self.voltage = self.interface.read_channel(channel=self.channel)
        else:
            # Mock out a random voltage!
            # Try and pull the mock otherwise use some defaults
            mock = self.config.get('mock', {})
            min_voltage = mock.get('min_voltage', 1.45)
            max_voltage = mock.get('max_voltage', 1.60)

            import random
            self.voltage = random.uniform(min_voltage, max_voltage)

    # Return the value that we want to display
    # Override this in the top level class
    def get_value(self):
        return self.voltage

    def __repr__(self):
        unit = 'voltage'
        return "<AnalogDevice: {value:0.2f}{unit}> ".format(
            value=self.get_value(),
            unit=unit
        )
