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

while True:
    fans.value(0)
    leds.value(0)
    pump.value(0)
    heater.value(0)

    time.sleep(5)

    fans.value(1)
    leds.value(1)
    pump.value(1)
    heater.value(1)

    time.sleep(5)

    print(measure.temp_hum(temp_hum))
    print(measure.soil(soil))
    