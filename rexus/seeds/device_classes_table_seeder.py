from orator.seeds import Seeder


class DeviceClassesTableSeeder(Seeder):

    table = 'device_classes'

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table(self.table).insert({
            'id': 1,
            'name': 'Raspberry Pi',
            'file': 'raspberry_pi'
        })

        self.db.table(self.table).insert({
            'id': 2,
            'name': 'ADC - pi-16adc',
            'file': 'adc_pi_16'
        })

        self.db.table(self.table).insert({
            'id': 3,
            'name': 'Generic Analog',
            'file': 'generic_analog_device'
        })

        self.db.table(self.table).insert({
            'id': 4,
            'name': 'Generic Digital',
            'file': 'generic_digital_device'
        })

        self.db.table(self.table).insert({
            'id': 5,
            'name': 'Soil Moisture - VH400',
            'file': 'soil_moisture_vh400'
        })
