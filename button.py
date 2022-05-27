import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.IN)
print("Press ctrl-c to stop.")
while(True):
	inputvalue=GPIO.input(18)
	if(inputvalue==False):
		print("Button pressed.")
		print("Start:%s" % time.ctime())
		time.sleep(1)
		print("End:%s" % time.ctime())
















