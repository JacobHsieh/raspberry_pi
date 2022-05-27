import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ledPin=18
GPIO.setup(ledPin,GPIO.OUT)
print("Press ctrl-c to stop.")

for i in range(20):
	print("LED turning on.")
	GPIO.output(ledPin,GPIO.HIGH)
	time.sleep(0.5)
	print("LED turning off.")
	GPIO.output(ledPin,GPIO.LOW)
	time.sleep(0.5)

