#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C

#  DroneBot Workshop 2019
#  https://dronebotworkshop.com

from smbus2 import SMBus, i2c_msg

import re

import json

import time

addr = 0x08 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

file = open('sensor_data.txt', 'a')

count = 0
while (count < 10):
        msg = i2c_msg.read(addr, 128)
        bus.i2c_rdwr(msg)
        l = list(msg) #read from esp and convert to list
        start = l.index(123) #get only the JSON section 
        end = l.index(125)
        l = l[start:end+1]
        res = ''.join(map(chr, l)) #convert to string
        file.write(res)
        file.write('\n')
        count = count + 1

file.close()
