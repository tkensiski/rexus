from orator.seeds import Seeder


class DeviceTypesTableSeeder(Seeder):

    table = 'device_types'

    def run(self):
        """
        Run the database seeds.
        """

        self.db.table(self.table).insert({
            'id': 1,
            'name': 'Raspberry Pi',
            'device_class_id': 1, # Raspberry Pi
            'model': '3 Model B',
            'description': ('The Raspberry Pi is a tiny and affordable computer that you can'
                            ' use to learn programming through fun, practical projects.')
        })

        self.db.table(self.table).insert({
            'id': 2,
            'model': 'TERM200',
            'device_class_id': 3, # Generic
            'name': 'Soil Temperature',
            'description': 'Soil Temperature probes that measure of how hot or cold the soil is'
        })

        self.db.table(self.table).insert({
            'id': 3,
            'model': '1124_0',
            'device_class_id': 3, # Generic
            'name': 'Air Temperature',
            'description': 'Air temperature sensors that measure of how hot or cold the air is'
        })

        self.db.table(self.table).insert({
            'id': 4,
            'model': 'VG-HUMID',
            'device_class_id': 3, # Generic
            'name': 'Relative Humidity',
            'description': ( 'Relative Humidity sensors to measure the amount of water vapor '
                             'present in air expressed as a percentage of the amount needed for '
                             'saturation at the same temperature.' )
        })

        self.db.table(self.table).insert({
            'id': 5,
            'model': 'Relay',
            'device_class_id': 4, # Generic
            'name': 'Relay',
            'description': ( 'Relays are electrical devices that typically incorporate an '
                             'electromagnet, that is activated by a current or signal in one '
                             'circuit to open or close another circuit.' )
        })

        self.db.table(self.table).insert({
            'id': 6,
            'model': '3551_0',
            'device_class_id': 3, # Generic
            'name': 'PH Meter',
            'description': ( 'PH Meters measure the difference in electrical potential between '
                             'a pH electrode and a reference electrode. The difference in '
                             'electrical potential relates to the acidity or pH of the solution.' )
        })

        self.db.table(self.table).insert({
            'id': 7,
            'model': 'pi-16adc',
            'device_class_id': 2, # ADC
            'name': 'ADC',
            'description': ( 'ADC - Analog to Digital Converter. ADCs provide an isolated '
                             'measurement such as an electronic device that converts an input '
                             'analog voltage or current to a digital number proportional to the '
                             'magnitude of the voltage or current.')
        })

        self.db.table(self.table).insert({
            'id': 8,
            'model': 'VH400',
            'device_class_id': 5, # Soil moisture VH400
            'name': 'Soil Moisture',
            'description': ( 'soil moisture sensor measures the quantity of water contained in a '
                              'material, such as soil on a volumetric or gravimetric basis' )
        })
