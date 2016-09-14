#!//usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time

from class_lux_de_emergencia import *

sistema = Lux_de_emergencia()

sistema.run_program()
