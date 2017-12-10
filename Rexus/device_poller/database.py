from influxdb import InfluxDBClient
from orator import DatabaseManager
from orator import Model

DATABASES = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'rexus',
        'user': 'rexus',
        'password': 'IDDrWO5iSmdbyt86',
        'prefix': ''
    },
    'influxdb': {
        'host': 'localhost',
        'port': '8086',
        'username': 'root',
        'password': 'root',
        'database': 'rexus'
    }
}

def configure_mysql():
    db = DatabaseManager(DATABASES)
    Model.set_connection_resolver(db)

def configure_influxdb():
    return InfluxDBClient(**DATABASES['influxdb'])
