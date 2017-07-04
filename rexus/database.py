from orator import DatabaseManager
from orator import Model

DATABASES = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'rexus',
        'user': 'rexus',
        'password': 'IDDrWO5iSmdbyt86',
        'prefix': ''
    }
}

def configure():
    db = DatabaseManager(DATABASES)
    Model.set_connection_resolver(db)
