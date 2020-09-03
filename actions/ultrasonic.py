from RPi import GPIO
import time


def find_distance(trig_pin: int, echo_pin: int):
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_pin, GPIO.LOW)

    startTime = time.time()
    endTime = time.time()

    while GPIO.input(echo_pin) == 0:
        startTime = time.time()
    
    while GPIO.input(echo_pin) == 1:
        endTime = time.time()
    
    timeDiff = endTime - startTime
    # in centimeter
    distance = (timeDiff * 34100)/2
    return distance

