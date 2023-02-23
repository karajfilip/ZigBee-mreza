#!/usr/bin/env python
import serial
from datetime import datetime
from time import sleep

ser = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)

print('starting')

for i in range(1, 61):
    print(i)
    ser.write(str(i)+' '+str(datetime.now())+'\n')
    sleep(1)

ser.close()
