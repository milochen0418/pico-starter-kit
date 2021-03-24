#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Origin: p48 at https://hackspace.raspberrypi.org/books/micropython-pico

import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    led_onboard.value(1)
    utime.sleep(5)
    led_onboard.value(0)
    utime.sleep(5)
