from RPi import GPIO as pi
from config.setting import init_sensor
from actions import motor, camera, infrared, ultrasonic
import time

pi.setmode(pi.BCM)
pwm = init_sensor()
LONG_LINE = 0

def long_line_decision():
    global LONG_LINE
    if LONG_LINE == 1:
        print("Exit from garage ...")
    elif LONG_LINE == 2:
        print("Select left lane ...")
    elif LONG_LINE == 3:
        print("Go to garage ...")
        motor.backward()
        time.sleep(0.3)
        motor.turn_left_90()
        motor.forward()
        time.sleep(3)

def drive():
    global LONG_LINE
    if infrared.should_turn_right():
        motor.turn_right()
    elif infrared.should_turn_left():
        motor.turn_left()
    elif infrared.should_long_line():
        LONG_LINE += 1
        motor.forward()
        time.sleep(0.2)
        long_line_decision()

    elif ultrasonic.should_stop():
        motor.dodge_barriere()
    motor.forward()

try:
    magazine_list = ["B1", "B2", "B3", "B4", "B5"]
    while True:
        drive()
        if len(magazine_list) > 0:
            qr_code = camera.get_qr_value()
            if qr_code in magazine_list:
                motor.stop()
                print("Shoot")
                magazine_list.remove(qr_code)

except KeyboardInterrupt:
    pwm.stop()
    pi.cleanup()

finally:
    pwm.stop()
    pi.cleanup()
