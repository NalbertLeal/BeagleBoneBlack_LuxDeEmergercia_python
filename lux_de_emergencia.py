#!//usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_12", GPIO.OUT)   # RGB red
GPIO.setup("P9_14", GPIO.OUT)   # RGB green
GPIO.setup("P9_16", GPIO.OUT)   # RGB blue
GPIO.setup("P9_18", GPIO.OUT)   # Red led
GPIO.setup("P9_27", GPIO.IN)    # button

while True:
    if GPIO.input("P9_27") == True:
        continue_loop = True
        time.sleep(1)
        while continue_loop:
            if GPIO.input("P9_27") == True:
                continue_loop = False
            photoresistor_path = open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw", "r+")
            photoresistorvalue = photoresistor_path.read()
            photo_int_value = int(photoresistorvalue)
            if photo_int_value < 1000:
                GPIO.output("P9_18", GPIO.LOW)   # turn on Red led
                potentiometer_path = open("/sys/bus/iio/devices/iio:device0/in_voltage1_raw", "r+")
                potentiometer_value = potentiometer_path.read()
                potentiometer_int_value = int(potentiometer_value)
                if potentiometer_int_value <= 1365:
                    GPIO.output("P9_12", GPIO.HIGH)   # RGB red as high
                    GPIO.output("P9_14", GPIO.LOW)   # RGB green as low
                    GPIO.output("P9_16", GPIO.LOW)   # RGB blue as low
                elif 1365 < potentiometer_int_value and potentiometer_int_value <= 2730:
                    GPIO.output("P9_12", GPIO.LOW)   # RGB red as low
                    GPIO.output("P9_14", GPIO.HIGH)   # RGB green as high
                    GPIO.output("P9_16", GPIO.LOW)   # RGB blue as low
                elif 2730 < potentiometer_int_value and potentiometer_int_value <= 4096:
                    GPIO.output("P9_12", GPIO.LOW)   # RGB red as low
                    GPIO.output("P9_14", GPIO.LOW)   # RGB green as low
                    GPIO.output("P9_16", GPIO.HIGH)   # RGB blue as high
            else:
                GPIO.output("P9_12", GPIO.LOW)   # RGB red as low
                GPIO.output("P9_14", GPIO.LOW)   # RGB green as low
                GPIO.output("P9_16", GPIO.LOW)   # RGB blue as high

                GPIO.output("P9_18", GPIO.HIGH)   # turn on Red led
    else:
        GPIO.output("P9_18", GPIO.LOW)   # turn on Red led
