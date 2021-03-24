#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Origin: p32 at https://hackspace.raspberrypi.org/books/micropython-pico

user_name = input ("What is your name? ")

while user_name != "Clark Kent":
    print("You are not Superman - try again!")
    user_name = input("What is your name? ")
print("You are Superman!")

