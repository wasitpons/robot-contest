from RPi import GPIO as pi
import time
from config.sensor import (
    LEFT_TRIG_GPIO,
    LEFT_ECHO_GPIO,
    MID_TRIG_GPIO,
    MID_ECHO_GPIO,
    RIGHT_TRIG_GPIO,
    RIGHT_TRIG_GPIO
)

def find_distance(trig_pin: int, echo_pin: int):
    pi.output(trig_pin, pi.HIGH)
    time.sleep(0.00001)
    pi.output(trig_pin, pi.LOW)

    startTime = time.time()
    endTime = time.time()

    while pi.input(echo_pin) == 0:
        startTime = time.time()
    
    while pi.input(echo_pin) == 1:
        endTime = time.time()
    
    timeDiff = endTime - startTime
    # in centimeter
    distance = (timeDiff * 34100)/2
    return distance

def get_distance():
    left_ultrasonic = find_distance(LEFT_TRIG_GPIO, LEFT_ECHO_GPIO)
    mid_ultrasonic = find_distance(MID_TRIG_GPIO, MID_ECHO_GPIO)
    right_ultrasonic = find_distance(RIGHT_TRIG_GPIO, RIGHT_TRIG_GPIO)
    return left_ultrasonic, mid_ultrasonic, right_ultrasonic

def should_stop():
    left, mid, right = get_distance()
    return (
        left <= 10 and
        mid <= 10 and
        right <= 10
    )