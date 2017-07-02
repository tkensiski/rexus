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
    55 : 2.92
}

# Flip them so we can look up stuff easier
soil_moisture_by_voltage = {}
for key, value in soil_moisture.iteritems():
    soil_moisture_by_voltage[str(value)] = key
