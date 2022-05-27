import RPi.GPIO as GPIO
import httplib, urllib
import time
import json

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ledPin=18
GPIO.setup(ledPin,GPIO.OUT)

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

while(True):
        print("LED turning on.")
	GPIO.output(ledPin,GPIO.HIGH)
	payload ={"datapoints":[{"dataChnId":"Button","values":{"value":1}}]}
	post_to_mcs(payload)
        time.sleep(5)
	print("LED turning off.")
	GPIO.output(ledPin,GPIO.LOW)
	payload ={"datapoints":[{"dataChnId":"Button","values":{"value":0}}]}
	post_to_mcs(payload)
        time.sleep(5)
	