import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
reading=0
GPIO.setup(17,GPIO.OUT)  #Refresh the capacitor
GPIO.output(17,False)
time.sleep(1)
GPIO.setup(17,GPIO.IN)
while(GPIO.input(17)==False):  #Break while when capacitor is full
	reading+=1      #test running to 245
	print(reading)

GPIO.cleanup()

