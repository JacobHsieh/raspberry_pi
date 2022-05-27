import RPi.GPIO as GPIO
import time

Control_pin=22
PWM_FREQ=50
STEP=15 #The angle that rotates everytime

GPIO.setmode(GPIO.BCM)
GPIO.setup(Control_pin,GPIO.OUT)

pwm=GPIO.PWM(Control_pin,PWM_FREQ)
pwm.start(0)

def angle_to_dutycycle(angle=0): #Angle and dutycycle transformation
	duty_cycle=(0.05*PWM_FREQ)+(0.19*PWM_FREQ*angle/180)
	return duty_cycle

try:
	print("Press ctrl-c to stop.")
	for angle in range(0,181,STEP):
		dc=angle_to_dutycycle(angle)
		pwm.ChangeDutyCycle(dc)
		print("Angle={:>3},DutyCycle={:.2f}".format(angle,dc))
		time.sleep(2)
	for angle in range(180,-1,-STEP):
                dc=angle_to_dutycycle(angle)
                pwm.ChangeDutyCycle(dc)
                print("Angle={:>3},DutyCycle={:.2f}".format(angle,dc))
                time.sleep(2)
	pwm.ChangeDutyCycle(angle_to_dutycycle(90))
	while(True): #Loop to let the angle stops at 90, and wait for Interrupt
		next

except KeyboardInterrupt:
	print("Stop.")
finally:
	pwm.stop()
	GPIO.cleanup()

