from rexus import database
from rexus.models import config, devices, device_classes, device_formulas, device_types


def main(influxdb):
    print "Config =========================="
    for conf in config.Config.all():
        print '{key}:{value}'.format(key=conf.key, value=conf.value)

    print "Devices =========================="
    for device in devices.Device.with_('device_type').get():
        print '{name} : {type}'.format(name=device.name, type=device.device_type.name)

    print "Device Types =========================="
    for device_type in device_types.DeviceType.with_('device_class').get():
        print '{name}:{class_name}:{description}'.format(
            name=device_type.name,
            description=device_type.description,
            class_name=device_type.device_class.name
        )

    print "Device Classes =========================="
    for device_class in device_classes.DeviceClass.get():
        print '{name}:{file}'.format(
            name=device_class.name,
            file=device_class.file
        )

    print "Device Formulas =========================="
    for device_formula in device_formulas.DeviceFormula.with_('device_type').get():
        print '{device_type}:{unit}:{formula}'.format(
            device_type=device_formula.device_type.name,
            unit=device_formula.unit,
            formula=device_formula.formula
        )

    print "Time Series DB =========================="
    for db in influxdb.get_list_database():
        print "{name}".format(name=db['name'])

if __name__ == '__main__':
    database.configure_mysql()
    influxdb = database.configure_influxdb()
    main(influxdb)
