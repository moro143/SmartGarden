import machine
import dht

def soil(pin):
    return pin.read()

def temp_hum(pin):
    pin.measure()
    return pin.temperature(), pin.humidity()