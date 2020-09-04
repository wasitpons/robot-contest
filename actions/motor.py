from RPi import GPIO
import time

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
    maxanum_forward(BACK_LEFT_FORWARD_GPIO, BACK_LEFT_BACKWARD_GPIO)
    maxanum_forward(FRONT_RIGHT_FORWARD_GPIO, FRONT_RIGHT_BACKWARD_GPIO)

def turn_right():
    maxanum_forward(FRONT_LEFT_FORWARD_GPIO, FRONT_LEFT_BACKWARD_GPIO)
    maxanum_forward(BACK_RIGHT_FORWARD_GPIO, BACK_RIGHT_BACKWARD_GPIO)

def right_slide():
    maxanum_forward(FRONT_LEFT_FORWARD_GPIO, FRONT_LEFT_BACKWARD_GPIO)
    maxanum_backward(FRONT_RIGHT_FORWARD_GPIO, FRONT_RIGHT_BACKWARD_GPIO)
    maxanum_backward(BACK_LEFT_FORWARD_GPIO, BACK_LEFT_BACKWARD_GPIO)
    maxanum_forward(BACK_RIGHT_FORWARD_GPIO, BACK_RIGHT_BACKWARD_GPIO)

def left_slide():
    maxanum_backward(FRONT_LEFT_FORWARD_GPIO, FRONT_LEFT_BACKWARD_GPIO)
    maxanum_forward(FRONT_RIGHT_FORWARD_GPIO, FRONT_RIGHT_BACKWARD_GPIO)
    maxanum_forward(BACK_LEFT_FORWARD_GPIO, BACK_LEFT_BACKWARD_GPIO)
    maxanum_backward(BACK_RIGHT_FORWARD_GPIO, BACK_RIGHT_BACKWARD_GPIO)

def turn_left_90():
    turn_left()
    time.sleep(0.4)

def turn_right_90():
    turn_right()
    time.sleep(0.4)

def dodge_barriere():
    right_slide()
    time.sleep(0.4)
    forward()
    time.sleep(0.3)
    left_slide()
    time.sleep(0.4)

def stop():
    maxanum_stop(BACK_LEFT_FORWARD_GPIO, BACK_LEFT_BACKWARD_GPIO)
    maxanum_stop(FRONT_LEFT_FORWARD_GPIO, FRONT_LEFT_BACKWARD_GPIO)
    maxanum_stop(BACK_RIGHT_FORWARD_GPIO, BACK_RIGHT_BACKWARD_GPIO)
    maxanum_stop(FRONT_RIGHT_FORWARD_GPIO, FRONT_RIGHT_BACKWARD_GPIO)
