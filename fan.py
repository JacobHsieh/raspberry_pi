import RPi.GPIO as GPIO
import time

fan_pin=37
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(fan_pin,GPIO.OUT)

while(True):
    GPIO.output(fan_pin,GPIO.HIGH)
    print("Turn off the fan.")
    time.sleep(3)
    GPIO.output(fan_pin,GPIO.LOW)
    print("Turn on the fan.")
    time.sleep(3)
    