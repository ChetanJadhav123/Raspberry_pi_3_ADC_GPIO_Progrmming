import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


def RC_Analog(Pin):
    counter = 0

    GPIO.setup(Pin, GPIO.OUT)
    GPIO.output(Pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(Pin, GPIO.IN)

    while(GPIO.input(Pin) == GPIO.LOW):
        counter = counter+1
    return counter


while True:
    print RC_Analog(4)


