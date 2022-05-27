import RPi.GPIO as GPIO
import time
import requests
import httplib, urllib
import json
import Adafruit_DHT
sys.path.append('/home/pi/rpi/code/Package')
DHT_sensor=Adafruit_DHT.DHT22
DHT_pin=15 #GPIO22 is connected to Data signal
LDR_pin=11
LED_pin=22
fan_pin=37
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_pin,GPIO.OUT)
GPIO.setup(fan_pin,GPIO.OUT)
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

def get_to_mcs(channelID):
  host = "http://api.mediatek.com"
  endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/" + channelID + "/datapoints"
  url = host + endpoint
  headers = {"Content-type": "application/json", "deviceKey": deviceKey}
  r = requests.get(url,headers=headers)
  value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
  return value

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

#Main Progress
while(True):
    humidity,temp=Adafruit_DHT.read_retry(DHT_sensor,DHT_pin)
    Lightlevel1=readLDR(LDR_pin)
    payload = {"datapoints":[{"dataChnId":"Humidity1","values":{"value":humidity}},{"dataChnId":"Temperature","values":{"value":temp}},{"dataChnId":"LightLevel1","values":{"value":Lightlevel1}}]}
    post_to_mcs(payload)
    Temperature2=get_to_mcs(Temperature2)
    Humidity2=get_to_mcs(Humidity2)
    Lightlevel2=get_to_mcs(LightLevel2)
    LightAutomation=get_to_mcs(LightAutomation)
    Temperature_Avg=(Temperature1+Temperature2)/2
    Humidity_Avg=(Humidity1+Humidity2)/2

    payload = {"datapoints":[{"dataChnId":"TempAvgtoFanControl","values":{"value":str(Temperature_Avg)}},{"dataChnId":"HumidityAvgtoFanCont","values":{"value":str(Humidity_Avg)}}]}
    post_to_mcs(payload)

    if(LightLevel1-Lightlevel2>0):
    	Lightlevel_min=Lightlevel2
    else:Lightlevel_min=Lightlevel1

    if(LightAutomation==1):
        print("Light automation activates.")
		PWM_LED(Lightlevel_min)

    else:
        print("Light automation deactivates.")
        PWM_LED(0)

     Fancontrol1=get_to_mcs(Fancontrol1)
     Fancontrol2=get_to_mcs(Fancontrol2)
     if(Fancontrol1 || Fancontrol2 ==1):
     	GPIO.output(fan_pin,GPIO.LOW)
        print("Turn on the fan.")
     else:
     	GPIO.output(fan_pin,GPIO.HIGH)
        print("Turn off the fan.")

