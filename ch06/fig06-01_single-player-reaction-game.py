#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Origin: p69 at https://hackspace.raspberrypi.org/books/micropython-pico

import machine
import utime
import urandom

pressed = False
led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

def button_handler(pin):
    global pressed
    if not pressed:
        pressed=True
        timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
        print("Your reaction time was " + str(timer_reaction) + " milliseconds!")

led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)
timer_start = utime.ticks_ms()
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

