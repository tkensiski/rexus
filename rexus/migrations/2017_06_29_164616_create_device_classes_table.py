from orator.migrations import Migration


class CreateDeviceClassesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('device_classes') as table:
            table.increments('id').unsigned()
            table.timestamps()
            table.string('name').unique()
            table.string('file')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('device_classes')
