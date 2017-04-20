device_map = {
    'device': {
        0: {
            'serial_number': 492043,
            'name': 'Rexus',
            'server_id': 'rexus',
            'server_port': 5001,
            'server_password': 'r3xu5!',
            'type_id': 0,
            'inputs': {
                'analog': {
                    # Input : Device ID
                    0: 2,
                    1: 3,
                    2: 4,
                    3: 5,
                    4: 7,
                    5: 8,
                    6: 9,
                    7: 10
                },
                'digital': {
                    0: None,
                    1: None,
                    2: None,
                    3: None,
                    4: None,
                    5: None,
                    6: None,
                    7: None
                },
            },
            'outputs': {
                0: 6,
                1: 11,
                2: 12,
                3: 13,
                4: 14,
                5: None,
                6: None,
                7: None
            }
        },
        1: {
            'serial_number': None, # TODO UPDATE THIS SHIT
            'name': 'Rexus Expansion',
            'type_id': 0,
            'inputs': {
                'analog': {
                    # Input : Device ID
                    0: None,
                    1: None,
                    2: None,
                    3: None,
                    4: None,
                    5: None,
                    6: None,
                    7: None
                },
                'digital': {
                    0: None,
                    1: None,
                    2: None,
                    3: None,
                    4: None,
                    5: None,
                    6: None,
                    7: None
                },
            },
            'outputs': {
                0: None,
                1: None,
                2: None,
                3: None,
                4: None,
                5: None,
                6: None,
                7: None
            }
        }
        2: {
            'name': 'Tent Right Temperature',
            'slug': 'Temp',
            'type_id': 3,
            'location_id': 1
        },
        3: {
            'name': 'Tent Right Soil Moisture',
            'slug': 'SWet',
            'type_id': 1,
            'location_id': 1
        },
        4: {
            'name': 'Tent Right Soil Temperature',
            'slug': 'STmp',
            'type_id': 2,
            'location_id': 1
        },
        5: {
            'name': 'Tent Right Relative Humidity',
            'slug': 'RHum',
            'type_id': 4,
            'location_id': 1
        },
        6: {
            'name': 'Tent Right Solinode',
            'slug': 'RTnt',
            'type_id': 5,
            'location_id': 1
        },
        7: {
            'name': 'Tent Left Temperature',
            'slug': 'Temp',
            'type_id': 3,
            'location_id': 0
        },
        8: {
            'name': 'Tent Left Soil Moisture',
            'slug': 'SWet',
            'type_id': 1,
            'location_id': 0
        },
        9: {
            'name': 'Tent Left Soil Temperature',
            'slug': 'STmp',
            'type_id': 2,
            'location_id': 0
        },
        10: {
            'name': 'Tent Left Relative Humidity',
            'slug': 'RH%',
            'type_id': 4,
            'location_id': 0
        },
        11: {
            'name': 'Tent Left Solinode',
            'slug': 'LTnt',
            'type_id': 5,
            'location_id': 0
        },
        12: {
            'name': 'Feed Line Solinode',
            'slug': 'Feed',
            'type_id': 5,
            'location_id': 3
        },
        13: {
            'name': 'Feed Pump',
            'slug': 'Pump',
            'type_id': 5,
            'location_id': 3
        },
        14: {
            'name': 'Air Stones',
            'slug': 'AStn',
            'type_id': 5,
            'location_id': 3
        },
        15: {
            'name': 'Feed Tank PH Electrode',
            'slug': 'PH',
            'type_id': 6,
            'location_id': 3
        },
        16: {
            'serial_number': 137633,
            'name': 'Tent Conditions Display',
            'slug': 'LCD',
            'type_id': 7,
            'location': 3
        }
    },
}

device_types = {
    0: 'interface_kit',
    1: 'soil_moisture',
    2: 'soil_temperature',
    3: 'temperature',
    4: 'relative_humidity',
    5: 'relay',
    6: 'ph_electrode',
    7: 'lcd_display'
}

locations = {
    0: { 'slug': 'LEFT', 'name': 'Left Tent' },
    1: { 'slug': 'RGHT', 'name': 'Right Tent' },
    3: { 'slug': 'WATR', 'name': 'Water Rack' },
    4: { 'slug': 'STOR', 'name': 'Storage' },
}