import os

from orator.seeds import Seeder


class ConfigTableSeeder(Seeder):

    table = 'config'

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table(self.table).insert({
            'key': 'name',
            'value': 'Rexus'
        })

        VERSION_FILE = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..', '..', 'VERSION'
        )
        with open(VERSION_FILE) as f:
            version = f.read().strip()

        self.db.table(self.table).insert({
            'key': 'version',
            'value': version
        })

        self.db.table(self.table).insert({
            'key': 'mock_channels',
            'value': 'True'
        })

        self.db.table(self.table).insert({
            'key': 'mock_interfaces',
            'value': 'True'
        })
