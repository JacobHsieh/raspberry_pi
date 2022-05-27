from hcsr04sensor import sensor
import time

TRIGGER_pin=25
ECHO_pin=8

try:
    print("Press ctrl-c to stop.")
    while(True):
        sr04=sensor.Measurement(TRIGGER_pin,ECHO_pin)
        raw_measurement=sr04.raw_distance()
        distance=sr04.distance_metric(raw_measurement)
        print("Distance is {:.1f} cm".format(distance))
        time.sleep(1)

except KeyboardInterrupt:
    print("Stop.")