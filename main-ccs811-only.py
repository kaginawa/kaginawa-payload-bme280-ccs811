#!/usr/bin/env python3

import sys
import time
import json

from ccs811 import CCS811


class AirConditionMonitor:
    CO2_PPM_THRESHOLD_1 = 1000
    CO2_PPM_THRESHOLD_2 = 2000

    CO2_LOWER_LIMIT = 400
    CO2_HIGHER_LIMIT = 8192

    CO2_STATUS_CONDITIONING = 'CONDITIONING'
    CO2_STATUS_LOW = 'LOW'
    CO2_STATUS_HIGH = 'HIGH'
    CO2_STATUS_TOO_HIGH = 'TOO HIGH'
    CO2_STATUS_ERROR = 'ERROR'

    def __init__(self):
        self._ccs811 = CCS811()
        self.co2_status = self.CO2_STATUS_LOW

    def status(self, co2):
        if co2 < self.CO2_LOWER_LIMIT or co2 > self.CO2_HIGHER_LIMIT:
            return self.CO2_STATUS_CONDITIONING
        elif co2 < self.CO2_PPM_THRESHOLD_1:
            return self.CO2_STATUS_LOW
        elif co2 < self.CO2_PPM_THRESHOLD_2:
            return self.CO2_STATUS_HIGH
        else:
            return self.CO2_STATUS_TOO_HIGH

    def available(self):
        return self._ccs811.available()

    def read_data(self):
        return self._ccs811.read_data()

    def get_eco2(self):
        return self._ccs811.get_eco2()

    def get_tvoc(self):
        return self._ccs811.get_tvoc()


def write_payload(temperature, humidity, pressure, co2, tvoc):
    payload = {"temperature": temperature, "humidity": humidity, "pressure": pressure, "co2": co2, "tvoc": tvoc,
               "timestamp": int(time.time())}
    with open("payload.json", "w") as f:
        json.dump(payload, f)


if __name__ == '__main__':
    co2_monitor = AirConditionMonitor()
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
                write_payload(None, None, None, co2, co2_monitor.get_tvoc())
            else:
                print('ERROR!')
                while True:
                    pass
        except:
            print(sys.exc_info())
        time.sleep(60)
