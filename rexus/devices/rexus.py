import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Rexus(object):
    def __init__(self, config):
        logger.debug('Initializing Rexus')

        if config is None:
            raise Exception('No config data for interface, cannot connect')

        logger.debug('config: {config}'.format(config=config))
        self.config = config

        # Make sure we keep track of what bus addresses that we init
        # so we dont init double and rather alert that theres a duplicate
        # address in use
        self.bus_addresses = []

        # interface_id: <DeviceType (Interface)>,
        self.interfaces = {}

    def is_conflicting_bus(self, bus_id, keep_track=True):
        """
        Check if the bus id is in conflict with another one before it
        """
        if bus_id in self.bus_addresses:
            return True

        if keep_track is True:
            self.bus_addresses.append(bus_id)

        return False

    def setup_interfaces(self):
        # Define this in the extended Rexus classes
        pass
