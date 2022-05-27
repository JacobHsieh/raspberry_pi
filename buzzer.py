import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO_PIN = 24
GPIO.setup(GPIO_PIN, GPIO.OUT)
#The software-PWM module will be initialized - a frequency of 500Hz will be taken as default.
Frequenz = 20000 #In Hertz
pwm = GPIO.PWM(GPIO_PIN, Frequenz)
pwm.start(50)
# The program will wait for the input of a new PWM-frequency from the user.
# Until then, the buzzer will be used with the before inputted frequency (default 500Hz).
try:
    while(True):
        for i in range(20000,20,-2000):
            Frequenz=i
            print "Current frequency: %d" % Frequenz
            pwm.ChangeFrequency(Frequenz)
            time.sleep(2)
         
# Scavenging work after the end of the program.
except KeyboardInterrupt:
    GPIO.cleanup()