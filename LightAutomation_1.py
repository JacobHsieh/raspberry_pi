import RPi.GPIO as GPIO
import time
import requests
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

def blinkLED(pin):
    GPIO.setup(pin,GPIO.OUT)
    print("Start blinking.")
    for i in range(10):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.5)

def PWM_LED(pin):
    GPIO.setup(pin,GPIO.OUT)
    PWM_FREQ=200
    pwm=GPIO.PWM(pin,PWM_FREQ)
    pwm.start(0) #Start control PWM and initialize to 0
    print("Start PWM mode.")
    for i in range(5):
        for duty_cycle in range(0,80,5):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
        for duty_cycle in range(80,0,-5):
	    pwm.ChangeDutyCycle(duty_cycle)
	    time.sleep(0.1)
    pwm.stop()

def get_to_mcs():
  host = "http://api.mediatek.com"
  endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/LightAutomation/datapoints"
  # url = ''.join([host,endpoint])
  url = host + endpoint
  headers = {"Content-type": "application/json", "deviceKey": deviceKey}
  r = requests.get(url,headers=headers)
  value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
  return value

def get_to_mcs_checkmode():
  host = "http://api.mediatek.com"
  endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/LEDmode/datapoints"
  # url = ''.join([host,endpoint])
  url = host + endpoint
  headers = {"Content-type": "application/json", "deviceKey": deviceKey}
  r = requests.get(url,headers=headers)
  value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
  return value # value=1 for Light, 2 for blink, 3 for PWM

def checkmode(num):
    if(num=='1'):
        switchonLED(LED_pin)
        print("LED switch on")
        time.sleep(1)
    elif(num=='2'):
        blinkLED(LED_pin)
        time.sleep(1)
    else:
        PWM_LED(LED_pin)
        time.sleep(1)
	
while(True):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    if(get_to_mcs()==1):
        print("Light automation activates.")
	LDR_reading=readLDR(LDR_pin)
	if(LDR_reading<LDR_threshold):
		switchoffLED(LED_pin)
		print("LED switch off")
		time.sleep(1)
	else:
            mode_value=get_to_mcs_checkmode()
            print(mode_value)
            checkmode(mode_value)
        time.sleep(3)

    else:
        print("Light automation deactivates.")
	switchoffLED(LED_pin)
	print("LED switch off")
        time.sleep(3)
        
    GPIO.cleanup()
