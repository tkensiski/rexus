import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class DeviceLoader(object):
    device_classes = {
        # device_type : getattr(module, class_name)
    }

    def load_device_class(self, device_type, device_class):
        logger.info('Loading class for device type: {device_type}'.format(
            device_type=device_type.name
        ))

        return self._load_device_class(device_type=device_type, device_class=device_class)

    def _load_device_class(self, device_type, device_class):
        if device_type in self.device_classes:
            logger.debug('Class already loaded for: {device_type}'.format(
                device_type=device_type.name
            ))

            return self.device_classes[device_type]

        # Build the module name
        module_name = 'rexus.devices.{name}'.format(name=device_class.file)

        # Import the module
        module = __import__(module_name, fromlist=[device_class.klass])

        # Get the class reference so we can use it later
        loaded_class = getattr(module, device_class.klass)

        # Memoize it for later
        self._memoize_device_class(device_type=device_type, loaded_class=loaded_class)

        # Pass it back so we can use it
        return loaded_class

    def _memoize_device_class(self, device_type, loaded_class):
        if device_type in self.device_classes:
            pass

        self.device_classes[device_type] = loaded_class
