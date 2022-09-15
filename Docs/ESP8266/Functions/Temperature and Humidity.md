d = dht.DHT22(machine.Pin(*num*))
d.measure()
d.temperature()
d.humidity()

d = dht.DHT22(machine.Pin(2))
d.measure()
d.temperature()
d.humidity()