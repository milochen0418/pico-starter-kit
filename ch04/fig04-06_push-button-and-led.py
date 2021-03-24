#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Origin: p55 at https://hackspace.raspberrypi.org/books/micropython-pico

import machine
import utime

led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led_external.value(1)
        utime.sleep(2)
    led_external.value(0)


