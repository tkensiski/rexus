from orator import DatabaseManager
from orator import Model

from rexus import config as app_config
from rexus.models import config, devices, device_classes, device_formulas, device_types


def setup_db():
    db = DatabaseManager(app_config.DATABASES)
    Model.set_connection_resolver(db)


def main():
    print "Config =========================="
    for conf in config.Config.all():
        print '{key}:{value}'.format(key=conf.key, value=conf.value)

    print "Devices =========================="
    for device in devices.Device.with_('device_type').get():
        print '{name} : {type}'.format(name=device.name, type=device.device_type.name)


if __name__ == '__main__':
    setup_db()
    main()
