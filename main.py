from RPi import GPIO as pi
from config.setting import init_sensor
from actions import movement

def clear_sensor():
    pi.cleanup()
    

try:
    pi.setmode(pi.BCM)
    init_sensor()
    while True:
        movement.forward()
except Exception as err:
    print(err)

finally:
    clear_sensor()

