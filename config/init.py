from RPi import GPIO
from config.sensor import (
    MAXANUM_POWER,
    BACK_LEFT_BACKWARD_GPIO,
    BACK_LEFT_ENA_GPIO,
    BACK_LEFT_FORWARD_GPIO
)

async def init_maxanum(ena_gpio, forward_gpio, backward_gpio):
    GPIO.setup(ena_gpio, GPIO.OUT)
    GPIO.setup(forward_gpio, GPIO.OUT)
    GPIO.setup(backward_gpio, GPIO.OUT)
    pwm=GPIO.PWM(ena_gpio, 1000)
    pwm.start(MAXANUM_POWER)


async def init_sensor():
    print("Set mode completed ..")
    await init_maxanum(
        ena_gpio=BACK_LEFT_ENA_GPIO,
        forward_gpio=BACK_LEFT_FORWARD_GPIO,
        backward_gpio=BACK_LEFT_BACKWARD_GPIO
    )
    print("Init port completed ..")

def clear_sensor():
    GPIO.cleanup()