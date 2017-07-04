from orator.migrations import Migration


class CreateDeviceTypesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('device_types') as table:
            table.increments('id').unsigned()
            table.timestamps()
            table.string('name').unique()
            table.string('model').unique()
            table.integer('device_class_id').unsigned()
            table.text('description')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('device_types')
