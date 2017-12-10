from orator.migrations import Migration


class CreateDevicesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('devices') as table:
            table.increments('id').unsigned()
            table.timestamps()
            table.integer('device_type_id').unsigned()
            table.string('name')
            table.json('config')

            table.unique(['name'])

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('devices')
