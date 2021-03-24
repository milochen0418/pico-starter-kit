#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Origin: p29 at https://hackspace.raspberrypi.org/books/micropython-pico

import utime

print("Loop starting!")

for i in range(10):
    print("Loop number", i)
    utime.sleep(1)

print("Loop finished!")
