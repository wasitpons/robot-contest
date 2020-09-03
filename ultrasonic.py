import RPi.GPIO as pi
import time

TRIG_PIN = 5
ECHO_PIN = 3

pi.setmode(pi.BOARD)
pi.setup(TRIG_PIN, pi.OUT)
pi.setup(ECHO_PIN, pi.IN)

def find_distance():
    pi.output(TRIG_PIN, pi.HIGH)
    time.sleep(0.00001)
    pi.output(TRIG_PIN, pi.LOW)

    startTime = time.time()
    endTime = time.time()

    while pi.input(ECHO_PIN) == 0:
        startTime = time.time()
    
    while pi.input(ECHO_PIN) == 1:
        endTime = time.time()
    
    timeDiff = endTime - startTime
    # in centimeter
    distance = (timeDiff * 34100)/2
    return distance

try: 
    while True:     
        distance = find_distance()
        print(f"Distance: {distance} cm")
        time.sleep(0.1)
except:
    pass
finally:
    pi.cleanup()
