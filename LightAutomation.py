import RPi.GPIO as GPIO
import time
import requests
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LDR_threshold=300     #Customized value depended on diffrent environment
LDR_pin=11
LED_pin=22

deviceId = "DYejquhT"
deviceKey = "3U0Sku0zmTIV2JDj"

def readLDR(pin):
	reading=0
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.LOW)  #Refresh the capacitor
	time.sleep(1)
	GPIO.setup(pin,GPIO.IN)    #Recharge the capacitor
	while(GPIO.input(pin)==GPIO.LOW):  #Break while when capacitor is full
		print(reading)
		reading+=1
	return reading

def switchonLED(pin):
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,True)

def switchoffLED(pin):
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,False)

def get_to_mcs():  
  host = "http://api.mediatek.com"
  endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/LightAutomation/datapoints"
  # url = ''.join([host,endpoint])
  url = host + endpoint
  headers = {"Content-type": "application/json", "deviceKey": deviceKey}
  r = requests.get(url,headers=headers)
  value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
  return value

while(True):
    if(get_to_mcs()==1):
        print("Light automation activates.")
	LDR_reading=readLDR(LDR_pin)
	if(LDR_reading<LDR_threshold):
		switchoffLED(LED_pin)
		print("LED switch off")
		time.sleep(1)
	else:
		switchonLED(LED_pin)
		print("LED switch on")
		time.sleep(1)
        time.sleep(3)
        
    if(get_to_mcs()==0):
        print("Light automation deactivates.")
	switchoffLED(LED_pin)
	print("LED switch off")
        time.sleep(3)