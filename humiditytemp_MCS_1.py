import time
import httplib, urllib
import json
import sys
import Adafruit_DHT
sys.path.append('/home/pi/rpi/code/Package')
DHT_sensor=Adafruit_DHT.DHT22
DHT_pin=22 #GPIO22 is connected to Data signal

#****************************************************
# Set Pin No, MediaTek Cloud Sandbox (MCS) Key
#****************************************************

deviceId = "DYejquhT"
deviceKey = "3U0Sku0zmTIV2JDj"

#****************************************************
# Set MediaTek Cloud Sandbox (MCS) Connection
#****************************************************

def post_to_mcs(payload):
    headers = {"Content-type": "application/json", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print("Error: %s" % ex)
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers)
    response = conn.getresponse()
    print( response.status, response.reason, json.dumps(payload), time.strftime("%c"))
    data = response.read()
    conn.close()

#****************************************************
# Post MediaTek Cloud Sandbox (MCS)
#****************************************************

while(True):
    humidity,temp=Adafruit_DHT.read_retry(DHT_sensor,DHT_pin)
    print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
    payload = {"datapoints":[{"dataChnId":"HumiditytoButton","values":{"value":str(humidity)}},{"dataChnId":"Temperature","values":{"value":temp}}]}
    post_to_mcs(payload)
    time.sleep(10)
