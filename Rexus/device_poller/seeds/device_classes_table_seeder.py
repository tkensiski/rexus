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
            'file': 'raspberry_pi',
            'klass': 'RaspberryPi'
        })

        self.db.table(self.table).insert({
            'id': 2,
            'name': 'ADC - pi-16adc',
            'file': 'adc_pi_16',
            'klass': 'ADC'
        })

        self.db.table(self.table).insert({
            'id': 3,
            'name': 'Generic Analog',
            'file': 'analog_device',
            'klass': 'AnalogDevice'
        })

        self.db.table(self.table).insert({
            'id': 4,
            'name': 'Generic Digital',
            'file': 'digital_device',
            'klass': 'DigitalDevice'
        })

        self.db.table(self.table).insert({
            'id': 5,
            'name': 'Soil Moisture - VH400',
            'file': 'soil_moisture_vh400',
            'klass': 'SoilMoisture'
        })
