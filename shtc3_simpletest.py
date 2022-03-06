#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Bryan Siepert for Adafruit Industries
# SPDX-FileCopyrightText: 2022 Chris Wilson <christopher.david.wilson@gmail.com>
#
# SPDX-License-Identifier: MIT
import time

import adafruit_shtc3
import board
import busio

i2c = busio.I2C(scl=board.pin.SCL, sda=board.pin.SDA)
sht = adafruit_shtc3.SHTC3(i2c)

while True:
    temperature, relative_humidity = sht.measurements
    print("Temperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % relative_humidity)
    print("")
    time.sleep(1)
