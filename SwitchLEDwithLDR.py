import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
LDR_threshold=300     #Customized value depended on diffrent environment
LDR_pin=11
LED_pin=22
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

while(True):
	LDR_reading=readLDR(LDR_pin)
	if(LDR_reading<LDR_threshold):
		switchoffLED(LED_pin)
		print("LED switch off")
	else:
		switchonLED(LED_pin)
		print("LED switch on")

	time.sleep(3)
