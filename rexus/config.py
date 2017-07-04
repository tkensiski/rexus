import logging

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

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
