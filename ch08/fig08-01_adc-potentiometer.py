#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Origin: p94 at https://hackspace.raspberrypi.org/books/micropython-pico

import machine
import utime

potentiometer = machine.ADC(26)

while True:
    print(potentiometer.read_u16())
    utime.sleep(2)

