
def connect_wifi(ssid, key):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, key)
        while not sta_if.isconnected():
            pass