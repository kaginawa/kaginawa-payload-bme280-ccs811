#!/usr/bin/env python3

import sys
import time
import json

from ccs811 import CCS811
import main

if __name__ == '__main__':
    co2_monitor = main.AirConditionMonitor()
    while not co2_monitor.available():
        pass
    while True:
        if not co2_monitor.available():
            time.sleep(1)
            continue
        try:
            if not co2_monitor.read_data():
                co2 = co2_monitor.get_eco2()
                co2_status = co2_monitor.status(co2)
                if co2_status == co2_monitor.CO2_STATUS_CONDITIONING:
                    time.sleep(2)
                    continue
                if co2_status != co2_monitor.co2_status:
                    co2_monitor.co2_status = co2_status
                main.write_payload(None, None, None, co2, co2_monitor.get_tvoc())
            else:
                print('ERROR!')
                while True:
                    pass
        except:
            print(sys.exc_info())
        time.sleep(60)
