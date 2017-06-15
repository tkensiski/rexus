import logging

name = 'Rexus'
version = '1.0.0' # Import this from VERSION

# Should we mock the channel data, useful for local development
mock_channels = True

display_units = 'imperial'

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

device_types = {
    """
    id: {
        'name': DEVICE_TYPE,
        # Optional, not required
        # see https://github.com/danthedeckie/simpleeval for more information
        # Must use {VOLTAGE} to have the voltage injected into the equation before
        # simple_eval is used
        'forumla': THE_FORMULA_TO_CONVERT_RAW_VOLTAGE_TO_VALUE
        # EX: '{VOTLAGE} * 200 * 0.2222 - 61.111'
        #
        # When a formula cannot be written and it involved more data
        # such as a lookup table we can specify the specific device file/class to use
        # 'device_file': 'soil_moisture_vh400',
        # 'device_class': 'SoilMoistureVH400'
    },
    """
    0: {
        'type': 'rasberry_pi',
        'model': '3 Model B',
        'formula': None
    },
    1: {
        'type': 'soil_moisture',
        'model': 'VH400',
        'forumla': None,
        'device_file': 'soil_moisture_vh400',
        'device_class': 'SoilMoistureVH400'
    },
    2: {
        'type': 'soil_temperature',
        'model': 'TERM200'
        'formula_imperial': "{VOTLAGE} * 75.006 - 40",
        'formula_metric' : "{VOTLAGE} * 41.67 - 40",
    },
    3: {
        'type': 'air_temperature',
        'formula_imperial': "({VOTLAGE} * 200 * 0.2222 - 61.111) * 9/5 + 32",
        'formula_metric': "{VOTLAGE} * 200 * 0.2222 - 61.111",
    },
    4: {
        'type': 'relative_humidity',
        'formula_imperial': "{VOTLAGE} * 33.33",
        'formula_metric': "{VOTLAGE} * 33.33",
    },
    5: { 'type': 'relay' },
    6: {
        'type': 'ph_electrode',
        'formula': "{VOTLAGE}",
    },
    8: { 'type': 'adc' }
}

# Move this to a database at some point
devices = {
    0: {
        'serial_number': '000000009dbced2f',
        'name': 'Rexus',
        'type_id': 0,
        'interface_ids': [ 1 ], # Device ids
    },
    1: {
        'name': 'ADC 1',
        'slug': 'adc1',
        'type_id': 8,
        'address': 76, # See rexus/config/ADC.py for more information on addresses
        'channels': {
            # channel # : Device ID
            0: 2,
            1: 3,
            2: 4,
            3: 5,
            4: 6,
            5: 7,
            6: 8,
            7: 9,
            8: 10,
            9: 11,
            10: 12,
            11: 13,
            12: None,
            13: None,
            14: None,
            15: None
        }
    }
    2: {
        'name': 'Temperature 1',
        'slug': 'Tmp1',
        'type_id': 3,
        # # Mock is optional, there is a default range set shown below
        # # if you want to define a different range just set these values
        # 'mock': {
        #     'min_voltage': 1.45,
        #     'max_voltage': 1.60,
        # },
    },
    3: {
        'name': 'Temperature 2',
        'slug': 'Tmp2',
        'type_id': 3,
    },
    4: {
        'name': 'Relative Humidity 1',
        'slug': 'RHu1',
        'type_id': 4,
    },
    5: {
        'name': 'Soil Moisture 1',
        'slug': 'SWet1',
        'type_id': 1,
    },
    6: {
        'name': 'Soil Moisture 2',
        'slug': 'SWet2',
        'type_id': 1,
    },
    7: {
        'name': 'Soil Moisture 3',
        'slug': 'SWet3',
        'type_id': 1,
    },
    8: {
        'name': 'Soil Moisture 4',
        'slug': 'SWet4',
        'type_id': 1,
    },
    9: {
        'name': 'Soil Moisture 5',
        'slug': 'SWet5',
        'type_id': 1,
    },
    10: {
        'name': 'Soil Moisture 6',
        'slug': 'SWet6',
        'type_id': 1,
    },
    11: {
        'name': 'Soil Moisture 7',
        'slug': 'SWet7',
        'type_id': 1,
    },
    12: {
        'name': 'Soil Moisture 8',
        'slug': 'SWet8',
        'type_id': 1,
    },
    13: {
        'name': 'Soil Moisture 9',
        'slug': 'SWet9',
        'type_id': 1,
    },
}
