from config.init import init_sensor, clear_sensor
from driver.movement import forward
from RPi import GPIO
from config.sensor import (
    MAXANUM_POWER,
    BACK_LEFT_BACKWARD_GPIO,
    BACK_LEFT_ENA_GPIO,
    BACK_LEFT_FORWARD_GPIO
)
import time

def init_maxanum(ena_gpio, forward_gpio, backward_gpio):
    GPIO.setup(ena_gpio, GPIO.OUT)
    GPIO.setup(forward_gpio, GPIO.OUT)
    GPIO.setup(backward_gpio, GPIO.OUT)
    pwm=GPIO.PWM(ena_gpio, 1000)
    pwm.start(MAXANUM_POWER)

try:
    clear_sensor()
    GPIO.setmode(GPIO.BCM)
    # GPIO.setup(BACK_LEFT_ENA_GPIO, GPIO.OUT)
    # GPIO.setup(BACK_LEFT_FORWARD_GPIO, GPIO.OUT)
    # GPIO.setup(BACK_LEFT_BACKWARD_GPIO, GPIO.OUT)
    # pwm=GPIO.PWM(BACK_LEFT_ENA_GPIO, 1000)
    # pwm.start(MAXANUM_POWER)
    # init_sensor()
    init_maxanum(
        ena_gpio=BACK_LEFT_ENA_GPIO,
        forward_gpio=BACK_LEFT_FORWARD_GPIO,
        backward_gpio=BACK_LEFT_BACKWARD_GPIO
    )
    time.sleep(0.1)
    while True:
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
except Exception as err:
    print(err)

finally:
    clear_sensor()