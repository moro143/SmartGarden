import machine
import dht
import time

fans = machine.Pin(14, machine.Pin.OUT)
leds = machine.Pin(12, machine.Pin.OUT)
pump = machine.Pin(13, machine.Pin.OUT)
heater = machine.Pin(2, machine.Pin.OUT)

temp_hum = dht.DHT22(machine.Pin(5))
soil = machine.ADC(0)

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

    temp_hum.measure()
    print(temp_hum.temperature())
    print(temp_hum.humidity())

    print(soil.read())
    