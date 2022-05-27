import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

PIR_pin=37
LED_pin=18
GPIO.setup(PIR_pin,GPIO.IN)
GPIO.setup(LED_pin,GPIO.OUT)

while(True):
    i=GPIO.input(PIR_pin)
    if(i==0):
        print("No intruder.")
        GPIO.output(LED_pin,GPIO.LOW)
        time.sleep(2)
    elif(i==1):
        print("Intruder detected.")
        GPIO.output(LED_pin,GPIO.HIGH)
        time.sleep(2)
