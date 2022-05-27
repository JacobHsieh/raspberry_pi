import RPi.GPIO as GPIO
import time

Monitorpin = 17 #number of GPIO(not on the board)
GPIO.setmode(GPIO.BCM)

try:
	print("press Ctrl-C then stop running")
	while(True):
		GPIO.setup(Monitorpin,GPIO.OUT)
		GPIO.output(Monitorpin,GPIO.LOW) #Refresh the capacitor
		time.sleep(0.5)

		count=0
		start_time=time.time()
		GPIO.setup(Monitorpin,GPIO.IN) #Recharge the capacitor
		while(GPIO.input(Monitorpin)==GPIO.LOW):
			count+=1
		end_time=time.time()

		print("count={},time={:.02f}".format(count,end_time-start_time))
except KeyboardInterrupt:
	print("Stop Running")
finally:
	GPIO.cleanup()

