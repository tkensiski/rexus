from orator.seeds import Seeder

from rexus.seeds.config_table_seeder import ConfigTableSeeder
from rexus.seeds.device_classes_table_seeder import DeviceClassesTableSeeder
from rexus.seeds.device_types_table_seeder import DeviceTypesTableSeeder
from rexus.seeds.device_formulas_table_seeder import DeviceFormulasTableSeeder
from rexus.seeds.devices_table_seeder import DevicesTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(ConfigTableSeeder)
        self.call(DeviceClassesTableSeeder)
        self.call(DeviceTypesTableSeeder)
        self.call(DeviceFormulasTableSeeder)
        self.call(DevicesTableSeeder)
