from RPi import GPIO as pi
from config.sensor import (
    LEFT_LED_GPIO,
    MID_LED_GPIO,
    RIGHT_LED_GPIO
)

WHITE = 1
BLACK = 0

def read_sensor():
    left = pi.input(LEFT_LED_GPIO)
    mid = pi.input(MID_LED_GPIO)
    right = pi.input(RIGHT_LED_GPIO)
    return left, mid, right

def should_turn_right():
    left_ir, mid_ir, right_ir = read_sensor()
    return (
        left_ir == WHITE and
        mid_ir == BLACK and 
        right_ir == BLACK
    )

def should_turn_left():
    left_ir, mid_ir, right_ir = read_sensor()
    return (
        left_ir == BLACK and
        mid_ir == BLACK and 
        right_ir == WHITE
    )

def should_long_line():
    left_ir, mid_ir, right_ir = read_sensor()
    return (
        left_ir == WHITE and
        mid_ir == WHITE and 
        right_ir == WHITE
    )