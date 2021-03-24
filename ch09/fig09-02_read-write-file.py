#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Origin: p106 at https://hackspace.raspberrypi.org/books/micropython-pico

file = open("test.txt", "w")
file.write("Hello, File!")
file.close()

file = open("test.txt")
file.read()
file.close()

