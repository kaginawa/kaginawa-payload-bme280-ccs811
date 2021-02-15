#!/usr/bin/env python3

import sys
import time
import json

import bme280
import main

if __name__ == '__main__':
    bme280.setup()
    bme280.get_calib_param()
    while True:
        try:
            t, h, p = bme280.read_data()
            main.write_payload(t, h, p, None, None)
        except:
            print(sys.exc_info())
        time.sleep(60)
