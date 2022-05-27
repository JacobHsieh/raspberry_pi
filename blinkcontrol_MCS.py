import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ledPin=18
GPIO.setup(ledPin,GPIO.OUT)

deviceId = "DYejquhT"
deviceKey = "3U0Sku0zmTIV2JDj"

def get_to_mcs():  
  host = "http://api.mediatek.com"
  endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/ButtonControl/datapoints"
  # url = ''.join([host,endpoint])
  url = host + endpoint
  headers = {"Content-type": "application/json", "deviceKey": deviceKey}
  r = requests.get(url,headers=headers)
  value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
  return value

while(True):
    if(get_to_mcs()==1):
        print("LED turning on.")
	GPIO.output(ledPin,GPIO.HIGH)
        time.sleep(0.5)
        
    if(get_to_mcs()==0):
        print("LED turning off.")
	GPIO.output(ledPin,GPIO.LOW)
        time.sleep(0.5)