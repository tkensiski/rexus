from rexus import database
from rexus.models import config, devices, device_classes, device_formulas, device_types


def main():
    print "Config =========================="
    for conf in config.Config.all():
        print '{key}:{value}'.format(key=conf.key, value=conf.value)

    print "Devices =========================="
    for device in devices.Device.with_('device_type').get():
        print '{name} : {type}'.format(name=device.name, type=device.device_type.name)


if __name__ == '__main__':
    database.configure()
    main()
