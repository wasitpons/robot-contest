from RPi import GPIO
from time import sleep
from config.sensor import (
    BACK_LEFT_FORWARD_GPIO,
    BACK_LEFT_BACKWARD_GPIO,
    FRONT_LEFT_FORWARD_GPIO,
    FRONT_LEFT_BACKWARD_GPIO,
    BACK_RIGHT_FORWARD_GPIO,
    BACK_RIGHT_BACKWARD_GPIO,
    FRONT_RIGHT_FORWARD_GPIO,
    FRONT_RIGHT_BACKWARD_GPIO
)

def maxanum_forward(forward_gpio, backward_gpio):
    GPIO.output(forward_gpio, GPIO.HIGH)
    GPIO.output(backward_gpio, GPIO.LOW)

def maxanum_backward(forward_gpio, backward_gpio):
    GPIO.output(forward_gpio, GPIO.LOW)
    GPIO.output(backward_gpio, GPIO.HIGH)

def maxanum_stop(forward_gpio, backward_gpio):
    GPIO.output(forward_gpio, GPIO.LOW)
    GPIO.output(backward_gpio, GPIO.LOW)

def forward():
    maxanum_forward(BACK_LEFT_FORWARD_GPIO, BACK_LEFT_BACKWARD_GPIO)
    maxanum_forward(FRONT_LEFT_FORWARD_GPIO, FRONT_LEFT_BACKWARD_GPIO)
    maxanum_forward(BACK_RIGHT_FORWARD_GPIO, BACK_RIGHT_BACKWARD_GPIO)
    maxanum_forward(FRONT_RIGHT_FORWARD_GPIO, FRONT_RIGHT_BACKWARD_GPIO)

def backward():
    maxanum_backward(BACK_LEFT_FORWARD_GPIO, BACK_LEFT_BACKWARD_GPIO)
    maxanum_backward(FRONT_LEFT_FORWARD_GPIO, FRONT_LEFT_BACKWARD_GPIO)
    maxanum_backward(BACK_RIGHT_FORWARD_GPIO, BACK_RIGHT_BACKWARD_GPIO)
    maxanum_backward(FRONT_RIGHT_FORWARD_GPIO, FRONT_RIGHT_BACKWARD_GPIO)

def turn_left():
    maxanum_backward(BACK_LEFT_FORWARD_GPIO, BACK_LEFT_BACKWARD_GPIO)
    maxanum_backward(FRONT_LEFT_FORWARD_GPIO, FRONT_LEFT_BACKWARD_GPIO)
    maxanum_forward(BACK_RIGHT_FORWARD_GPIO, BACK_RIGHT_BACKWARD_GPIO)
    maxanum_forward(FRONT_RIGHT_FORWARD_GPIO, FRONT_RIGHT_BACKWARD_GPIO)

def turn_right():
    maxanum_forward(BACK_LEFT_FORWARD_GPIO, BACK_LEFT_BACKWARD_GPIO)
    maxanum_forward(FRONT_LEFT_FORWARD_GPIO, FRONT_LEFT_BACKWARD_GPIO)
    maxanum_backward(BACK_RIGHT_FORWARD_GPIO, BACK_RIGHT_BACKWARD_GPIO)
    maxanum_backward(FRONT_RIGHT_FORWARD_GPIO, FRONT_RIGHT_BACKWARD_GPIO)

def stop():
    maxanum_stop(BACK_LEFT_FORWARD_GPIO, BACK_LEFT_BACKWARD_GPIO)
    maxanum_stop(FRONT_LEFT_FORWARD_GPIO, FRONT_LEFT_BACKWARD_GPIO)
    maxanum_stop(BACK_RIGHT_FORWARD_GPIO, BACK_RIGHT_BACKWARD_GPIO)
    maxanum_stop(FRONT_RIGHT_FORWARD_GPIO, FRONT_RIGHT_BACKWARD_GPIO)