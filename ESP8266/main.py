# Importing settings
import json
file = open('settings.json')
settings = json.load(file)

import machine
import dht
import time

# Trying to connect to WiFi if known
import ESP_control
ssid = settings["Device"]["WiFi"]["SSID"]
key = settings["Device"]["WiFi"]["Key"]
if ssid!="":
    ESP_control.connect_wifi(ssid, key)

fans = machine.Pin(14, machine.Pin.OUT)
leds = machine.Pin(12, machine.Pin.OUT)
pump = machine.Pin(13, machine.Pin.OUT)
heater = machine.Pin(2, machine.Pin.OUT)

temp_hum = dht.DHT22(machine.Pin(5))
soil = machine.ADC(0)

import measure

old_time = time.time()
TIMESTEP = 0.05

is_day = True
day_time = settings['User']['Day night cycle']['Day hours'] * 60 * 60
night_time = settings['User']['Day night cycle']['Night hours'] * 60 * 60

while True:
    if (time.time() - old_time) > TIMESTEP:         # Enter loop every TIMESTEP seconds
        old_time = time.time()

        # Basic day night cycle
        if is_day:
            leds.value(0)
            day_time -= TIMESTEP
            if day_time <= 0:
                is_day = False
                day_time = settings['User']['Day night cycle']['Day hours'] * 60 * 60
        else:
            leds.value(1)
            night_time -= TIMESTEP
            if night_time <= 0:
                is_day = True
                night_time = settings['User']['Day night cycle']['Night hours'] * 60 * 60

        c_temp, c_hum = measure.temp_hum(temp_hum)
        c_soil = measure.soil(soil)
        
        # Heater and fans basic automation
        if settings['User']['Temperature'][0]<=c_temp<=settings['User']['Temperature'][1]:
            fans.value(1)
            heater.value(1)
        elif settings['User']['Temperature'][0]>c_temp:
            heater.value(0)
        elif settings['User']['Temperature'][1]<c_temp:
            fans.value(0)

        # Pump basic automation
        if c_soil >= settings['User']['Soil']:
            pump.value(1)
        else:
            pump.value(0)