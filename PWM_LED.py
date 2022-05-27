import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
LED_pin=22
PWM_FREQ=200

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_pin,GPIO.OUT)

pwm=GPIO.PWM(LED_pin,PWM_FREQ)
pwm.start(0) #Start control PWM and initialize to 0

try:
	print("Press ctrl-c to stop running.")
	while(True):
		for duty_cycle in range(0,100,5):
			pwm.ChangeDutyCycle(duty_cycle)
			time.sleep(0.2)
		for duty_cycle in range(100,0,-5):
			pwm.ChangeDutyCycle(duty_cycle)
			time.sleep(0.2)
except KeyboardInterrupt:
	print("Stop")
finally:
	pwm.stop()
	GPIO.cleanup()
