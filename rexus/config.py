#!/usr/bin/env python
display_units = 'imperial'

# VWC to Voltage of the sensor
# Number of points will dictate the Human readable % so that way after a 
# watering it will read 100% for a period of time
# How To Get Datapoints: http://www.vegetronix.com/TechInfo/How-To-Measure-VWC.phtml
soil_moisture = {
    # Volumetric Water Content (vwc): Sensor Voltage (v)
    # x : y
     0 : 0.26,
     5 : 0.65,
    10 : 1.05,
    15 : 1.25,
    20 : 1.64,
    25 : 1.85,
    30 : 2.00,
    35 : 2.10,
    40 : 2.38,
    45 : 2.50,
    50 : 2.60,
    55 : 2.92,
    60 : 3.00
}

# Flip them so we can look up stuff easier
soil_moisture_by_voltage = {}
for key, value in soil_moisture.iteritems():
    soil_moisture_by_voltage[str(value)] = key

device_map = {
    'device': {
        0: {
            'name': 'rexus',
            'type': 'InterfaceKit',
            'inputs': {
                'analog': {
                    # Input : Device ID
                    0: None,
                    1: None,
                    2: None,
                    3: None,

                    4: { 'type': 'temperature_air',   'location': 1 },
                    5: { 'type': 'temperature_soil',  'location': 1 },
                    6: { 'type': 'relative_humidity', 'location': 1 },
                    7: { 'type': 'moisture_soil',     'location': 1 },
                },
                'digital': {
                    0: { 'type': 'pump', 'location': None },
                    1: { 'type': 'relay', 'location': None },
                    2: { 'type': 'relay', 'location': None },
                    3: { 'type': 'relay', 'location': None },
                    4: { 'type': 'relay', 'location': None },
                    5: { 'type': 'relay', 'location': None },
                    6: { 'type': 'relay', 'location': None },
                    7: { 'type': None, 'location': None },
                },
            },
        },
        1: {

        },
    },
}

device_types = {
    0: 'interface_kit',
    1: 'soil_moisture',
    2: 'soil_temperature',
    3: 'temperature',
    4: 'relative_humidity',
    5: 'relay',
    6: 'transfer_pump',
    7: 'paralistic_pump',
    8: 'ph_electrode',

}

locations = {
    0: { 'slug': 'LEFT', 'name': 'Left Tent' },
    1: { 'slug': 'RGHT', 'name': 'Right Tent' },
    3: { 'slug': 'WATR', 'name': 'Water Rack' },
    4: { 'slug': 'STOR', 'name': 'Storage' },
}