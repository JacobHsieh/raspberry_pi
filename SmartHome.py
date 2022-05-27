import RPi.GPIO as GPIO
import time
import requests
LDR_pin=11
LED_pin=22
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_pin,GPIO.OUT)
PWM_FREQ=200
pwm=GPIO.PWM(LED_pin,PWM_FREQ)
pwm.start(0) #Start control PWM and initialize to 0

deviceId = "DYejquhT"
deviceKey = "3U0Sku0zmTIV2JDj"

def readLDR(pin):
	reading=0
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.LOW)  #Refresh the capacitor
	time.sleep(1)
	GPIO.setup(pin,GPIO.IN)    #Recharge the capacitor
	while(GPIO.input(pin)==GPIO.LOW):  #Break while when capacitor is full
		reading+=1
        print(reading)
	return reading

def PWM_LED(lightlevel):
    duty_cycle=lightlevel/100 #duty_cycle:0~100
    if(duty_cycle>=100):duty_cycle=100
    pwm.ChangeDutyCycle(duty_cycle)

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
	PWM_LED(LDR_reading)
        time.sleep(7)

    else:
        print("Light automation deactivates.")
        PWM_LED(0)
	print("LED switch off")
        time.sleep(3)
