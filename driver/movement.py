from RPi import GPIO
from config.sensor import (
    BACK_LEFT_FORWARD_GPIO,
    BACK_LEFT_BACKWARD_GPIO
)
from time import sleep

def maxanum_forward(forward_gpio, backward_gpio):
    print("forward 1")
    GPIO.output(forward_gpio, GPIO.HIGH)
    GPIO.output(backward_gpio, GPIO.LOW)
    sleep(0.1)

def maxanum_backward(forward_gpio, backward_gpio):
    GPIO.output(forward_gpio, GPIO.LOW)
    GPIO.output(backward_gpio, GPIO.HIGH)

def maxanum_stop(forward_gpio, backward_gpio):
    GPIO.output(forward_gpio, GPIO.LOW)
    GPIO.output(backward_gpio, GPIO.LOW)

def forward():
    maxanum_forward(BACK_LEFT_FORWARD_GPIO, BACK_LEFT_BACKWARD_GPIO)