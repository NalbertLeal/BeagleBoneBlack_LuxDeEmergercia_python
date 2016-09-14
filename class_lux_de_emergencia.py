#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time

class Lux_de_emergencia:

    def __init__(self):
        GPIO.setup("P9_12", GPIO.OUT)   # RGB red
        GPIO.setup("P9_14", GPIO.OUT)   # RGB green
        GPIO.setup("P9_16", GPIO.OUT)   # RGB blue
        GPIO.setup("P9_18", GPIO.OUT)   # Red led
        GPIO.setup("P9_27", GPIO.IN)    # button

    def turn_on_red_led(self):
        GPIO.output("P9_18", GPIO.HIGH)   # turn on Red led

    def turn_off_red_led(self):
        GPIO.output("P9_18", GPIO.LOW)   # turn off Red led

    def turn_on_RGB_red(self):
        GPIO.output("P9_12", GPIO.HIGH)   # RGB red as high
        GPIO.output("P9_14", GPIO.LOW)   # RGB green as low
        GPIO.output("P9_16", GPIO.LOW)   # RGB blue as low

    def turn_on_RGB_green(self):
        GPIO.output("P9_12", GPIO.LOW)   # RGB red as low
        GPIO.output("P9_14", GPIO.HIGH)   # RGB green as high
        GPIO.output("P9_16", GPIO.LOW)   # RGB blue as low

    def turn_on_RGB_blue(self):
        GPIO.output("P9_12", GPIO.LOW)   # RGB red as low
        GPIO.output("P9_14", GPIO.LOW)   # RGB green as low
        GPIO.output("P9_16", GPIO.HIGH)   # RGB blue as high

    def turn_off_RGB(self):
        GPIO.output("P9_12", GPIO.LOW)   # RGB red as low
        GPIO.output("P9_14", GPIO.LOW)   # RGB green as low
        GPIO.output("P9_16", GPIO.LOW)   # RGB blue as high

    def get_button(self):
        return GPIO.input("P9_27")

    def run_program(self):
        while True:
            if self.get_button() == True:
                continue_loop = True
                time.sleep(1)
                if self.get_button() == True:
                    return 0
                while continue_loop:
                    if self.get_button() == True:
                        continue_loop = False
                    photoresistor_path = open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw", "r+")
                    photoresistorvalue = photoresistor_path.read()
                    photo_int_value = int(photoresistorvalue)
                    if photo_int_value < 1000:
                        self.turn_off_red_led()
                        potentiometer_path = open("/sys/bus/iio/devices/iio:device0/in_voltage1_raw", "r+")
                        potentiometer_value = potentiometer_path.read()
                        potentiometer_int_value = int(potentiometer_value)
                        if potentiometer_int_value <= 1365:
                            self.turn_on_RGB_red()
                        elif 1365 < potentiometer_int_value and potentiometer_int_value <= 2730:
                            self.turn_on_RGB_green()
                        else:
                            self.turn_on_RGB_blue()
                    else:
                        self.turn_off_RGB()

                        self.turn_on_red_led()
            else:
                self.turn_off_RGB()
                self.turn_off_red_led()
