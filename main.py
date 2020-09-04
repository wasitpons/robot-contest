from RPi import GPIO as pi
from config.setting import init_sensor
from actions import motor, camera, infrared
import time

pi.setmode(pi.BCM)
pwm = init_sensor()

def drive():
    if infrared.should_turn_right():
        motor.turn_right()
    elif infrared.should_turn_left():
        motor.turn_left()
    motor.forward()

try:
    while True:
        drive()
        qr_code = camera.get_qr_value()
        if qr_code is not None:
            print("Do something...")

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    pi.cleanup()
