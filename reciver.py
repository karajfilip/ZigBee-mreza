#!/usr/bin/env python3
from datetime import datetime
import serial
import time

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

while True:
    try:
        incoming = ser.readline().strip()
        if(incoming!=''):
            print('data: '+incoming+str(datetime.now()))

    except KeyboardInterrupt:
        break

ser.close()
