#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Origin: p82 at https://hackspace.raspberrypi.org/books/micropython-pico

import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("ALARM! Motion detected!")

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

