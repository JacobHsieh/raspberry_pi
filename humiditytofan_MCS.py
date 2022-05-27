import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
fan_pin=37
GPIO.setup(fan_pin,GPIO.OUT)

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
        GPIO.output(fan_pin,GPIO.LOW)
        print("Turn on the fan.")
        time.sleep(3)
        
    if(get_to_mcs()==0):
        GPIO.output(fan_pin,GPIO.HIGH)
        print("Turn off the fan.")
        time.sleep(3)
