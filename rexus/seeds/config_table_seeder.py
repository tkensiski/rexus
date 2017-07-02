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

        self.db.table(self.table).insert({
            'key': 'version',
            'value': 'True'
        })

        self.db.table(self.table).insert({
            'key': 'mock_channels',
            'value': 'True'
        })

