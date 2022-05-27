import time
import Adafruit_DHT

DHT_sensor=Adafruit_DHT.DHT22
DHT_pin=22 #GPIO22 is connected to Data signal

while(True):
	humidity,temperature=Adafruit_DHT.read_retry(DHT_sensor,DHT_pin)
	#the "read_retry" continually try to retrieve the data from sensor
	if(humidity is not None and temperature is not None): #Data in return
		print('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'),time.strftime('%H:%M'),temperature,humidity))
	else:
		print("Failed to retrieve data from the sensor")
	
	time.sleep(3)

GPIO.cleanup()

