from orator.seeds import Seeder
import json


class DevicesTableSeeder(Seeder):

    table = 'devices'

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table(self.table).insert({
            'id': 1,
            'name': 'Rexus',
            'device_type_id': 1,
            'config': json.dumps({
                "interface_ids": [2]
            })
        })

        self.db.table(self.table).insert({
            'id': 2,
            'name': 'ADC',
            'device_type_id': 7,
            'config': json.dumps({
                'address': 76,
                'channels': {
                    # channel # : Device ID
                    0: None,
                    1: None,
                    2: None,
                    3: None,
                    4: None,
                    5: None,
                    6: None,
                    7: None,
                    8: None,
                    9: None,
                    10: None,
                    11: None,
                    12: None,
                    13: None,
                    14: None,
                    15: None
                }
            })
        })

        self.db.table(self.table).insert({
            'device_type_id': 3,
            'name': 'Air Temp',
            'config': json.dumps({})
        })

        self.db.table(self.table).insert({
            'device_type_id': 4,
            'name': 'Relative Humidity',
            'config': json.dumps({})
        })

        self.db.table(self.table).insert({
            'device_type_id': 8,
            'name': 'Soil Moisture',
            'config': json.dumps({})
        })

        self.db.table(self.table).insert({
            'device_type_id': 2,
            'name': 'Soil Temp',
            'config': json.dumps({})
        })
