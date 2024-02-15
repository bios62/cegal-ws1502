# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""CircuitPython blink example for built-in NeoPixel LED"""
import wifi   # should be first to reduce of memory issues
import time
import board
import neopixel
import ssl
import socketpool
import adafruit_requests
import adafruit_ahtx0
import supervisor
import gc


# Add the corret ATP ORDS REST URL
# Example format https://hirokixxx-mydb.adb.eu-frankfurt-1.oraclecloudapps.com/ords/demouser5/wsapi/temp

JSON_POST_URL = "https://<your ATP URL>/ords/<username>/wsapi/temp"


print ("\nstart:")
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
print (gc.mem_free())
if (gc.mem_free()<2023000):
    print("\nMemory restart -Green->Red")
    for x in range(255):
        pixel.fill((x, 255 - x, 0))
        time.sleep(0.1)
        supervisor.reload()
print("\nStart - white->green")
for x in range(255):
    pixel.fill((255 - x, 255, 255 - x))
    time.sleep(0.1)
restartCnt = 0
while True:
    restartCnt = restartCnt + 1
    print(f"restartCnt: {restartCnt} ")
    if (restartCnt > 10):
        print("restart - restartCnt - white 20 sec")
        pixel.fill((255, 255, 255))
        time.sleep(20.0)
        supervisor.reload()
    print("\nLoop Start - white 2 sec")
    connectWiFi = False
    pixel.fill((255, 255, 255))
    time.sleep(2.0)
    print(f"My MAC address: {[hex(i) for i in wifi.radio.mac_address]}")

    pixel.fill((0, 255, 255))
    time.sleep(2.0)
    print("Available WiFi networks:")

    for network in wifi.radio.start_scanning_networks():
        print(
            "\t%s\t\tRSSI: %d\tChannel: %d"
            % (str(network.ssid, "utf-8"), network.rssi, network.channel)
        )
    wifi.radio.stop_scanning_networks()

    print(f"Connecting to wifi")
    try:
	# change wifi SSID and PWD in next line
        ssid="MYSSID"
        pwd="MYPWD"
        wifi.radio.connect(ssid,pwd)
        connectWiFi = True
    except:
        print("\nConnect to network - failed")
    print(f"\nConnected to wifi")
    print(connectWiFi)
    print(f"My IP address: {wifi.radio.ipv4_address}")

    pixel.fill((255, 0, 255))
    time.sleep(2.0)
    try:
        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())
    except:
        print("\nrequests error - exception")

    pixel.fill((255, 255, 0))
    time.sleep(2.0)
    mc = 22
    try:
        i2c = board.STEMMA_I2C()
        aht20 = adafruit_ahtx0.AHTx0(i2c)
        data = [aht20.temperature, aht20.relative_humidity]
        print("\nTemperature: %0.1f C" % aht20.temperature)
        # mc = int(aht20.temperature * 1000)
        mc = aht20.temperature
        print("\nTemperature mc: %0.1f C" % mc)
        print("\nHumidity: %0.1f %%" % aht20.relative_humidity)
        print()
    except:
        print("\nNo sensor - default temperature:%0.1f C" % mc)
        print("Yellow/Red - Blink")
        pixel.fill((255, 255, 0))
        time.sleep(1.5)
        pixel.fill((255, 0, 0))
        time.sleep(1.5)
        pixel.fill((255, 255, 0))
        time.sleep(1.5)
        pixel.fill((255, 0, 0))
        time.sleep(1.5)


    pixel.fill((255, 255, 0))
    print("Yellow")
    time.sleep(1.5)
    # myobj = {"objectname": "PYTHON", "sensorname": "TempMC", "sensorvalue": mc}
    myobj = {"temp": mc}
    print(myobj)

    if connectWiFi:
        print("\nPost Autonomous...")
        try:
            header={"Content-Type": "application/json"}
            print("-" * 40)
            # print(f"Test prediction: {response.json()}")
            # response = requests.post(JSON_POST_URL, header=header, json=myobj)
            response = requests.post(JSON_POST_URL, json=myobj)
            print(response.status_code)
            print("-" * 40)
            # print(f"Test prediction: {response.json()}")
            print("\nPost Autonomus - OK - Green 30 sec")
            print (gc.mem_free())
            pixel.fill((0, 255, 0))
            time.sleep(30)
        except Exception as e:
            print (e)
            print("\nPost Autonomous - Exception - Red")
            pixel.fill((255, 0, 0))
            print (gc.mem_free())
            time.sleep(10)
            supervisor.reload()
        print("\nPost Autonomous - OK - supervisor.reload : Green -> blue")
        

        for x in range(255):
            pixel.fill((0, 255 - x, x))
            time.sleep(0.025)
        supervisor.reload()
    else:
        print("\nPost Autonomous - canceled - no IP - blue")
        pixel.fill((0, 0, 255))
        time.sleep(10)
    for x in range(255):
        pixel.fill((x, x, x))
        time.sleep(0.01)
    
    for x in range(255):
        pixel.fill((x, 255 - x, 0))
        time.sleep(0.025)
  
