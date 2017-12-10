from orator.migrations import Migration


class CreateDeviceFormulasTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('device_formulas') as table:
            table.increments('id').unsigned()
            table.timestamps()
            table.integer('device_type_id').unsigned()
            table.string('formula')
            table.string('unit', 4)

            table.unique(['device_type_id', 'unit'])

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('device_formulas')
