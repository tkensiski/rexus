from orator.seeds import Seeder


class DeviceFormulasTableSeeder(Seeder):

    table = 'device_formulas'

    def run(self):
        """
        Run the database seeds.
        """

        self.db.table(self.table).insert({
            'device_type_id': 2, # Soil Temperature
            'formula': "{VOTLAGE} * 75.006 - 40",
            'unit': 'F'
        })

        self.db.table(self.table).insert({
            'device_type_id': 2, # Soil Temperature
            'formula': "{VOTLAGE} * 41.67 - 40",
            'unit': 'C'
        })

        self.db.table(self.table).insert({
            'device_type_id': 3, # Air Temperature
            'formula': "({VOTLAGE} * 200 * 0.2222 - 61.111) * 9/5 + 32",
            'unit': 'F'
        })

        self.db.table(self.table).insert({
            'device_type_id': 3, # Air Temperature
            'formula': "{VOTLAGE} * 200 * 0.2222 - 61.111",
            'unit': 'C'
        })

        self.db.table(self.table).insert({
            'device_type_id': 4, # Relative Humidity
            'formula':"{VOTLAGE} * 33.33",
            'unit': 'RH%'
        })
