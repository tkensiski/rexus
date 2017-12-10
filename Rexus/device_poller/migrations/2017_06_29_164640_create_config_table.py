from orator.migrations import Migration


class CreateConfigTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('config') as table:
            table.increments('id').unsigned()
            table.timestamps()
            table.string('key').unique()
            table.string('value')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('config')
