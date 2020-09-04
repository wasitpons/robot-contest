from RPi import GPIO as pi
from config.sensor import (
    MAXANUM_POWER,
    ENA_GPIO,
    BACK_LEFT_FORWARD_GPIO,
    BACK_LEFT_BACKWARD_GPIO,
    FRONT_LEFT_FORWARD_GPIO,
    FRONT_LEFT_BACKWARD_GPIO,
    BACK_RIGHT_FORWARD_GPIO,
    BACK_RIGHT_BACKWARD_GPIO,
    FRONT_RIGHT_FORWARD_GPIO,
    FRONT_RIGHT_BACKWARD_GPIO
)

def init_sensor():
    pi.setup(ENA_GPIO, pi.OUT)
    pwm=pi.PWM(ENA_GPIO, 1000)
    pwm.start(MAXANUM_POWER)

    pi.setup(BACK_LEFT_FORWARD_GPIO, pi.OUT)
    pi.setup(BACK_LEFT_BACKWARD_GPIO, pi.OUT)

    pi.setup(FRONT_LEFT_FORWARD_GPIO, pi.OUT)
    pi.setup(FRONT_LEFT_BACKWARD_GPIO, pi.OUT)

    pi.setup(BACK_RIGHT_FORWARD_GPIO, pi.OUT)
    pi.setup(BACK_RIGHT_BACKWARD_GPIO, pi.OUT)

    pi.setup(FRONT_RIGHT_FORWARD_GPIO, pi.OUT)
    pi.setup(FRONT_RIGHT_BACKWARD_GPIO, pi.OUT)
    return pwm