from RPi import GPIO as pi
from config.setting import init_sensor
from actions import movement, camera
import time

pwm = init_sensor()

try:
    pi.setmode(pi.BCM)
    while True:
        movement.turn_right_90()
        qr_code = camera.get_qr_value()
        print(qr_code)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    pi.cleanup()
