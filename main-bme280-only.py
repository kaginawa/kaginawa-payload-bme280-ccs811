#!/usr/bin/env python3

import sys
import time
import json

import bme280


def write_payload(temperature, humidity, pressure, co2, tvoc):
    payload = {"temperature": temperature, "humidity": humidity, "pressure": pressure, "co2": co2, "tvoc": tvoc,
               "timestamp": int(time.time())}
    with open("payload.json", "w") as f:
        json.dump(payload, f)


if __name__ == '__main__':
    bme280.setup()
    bme280.get_calib_param()
    while True:
        try:
            t, h, p = bme280.read_data()
            write_payload(t, h, p, None, None)
        except:
            print(sys.exc_info())
        time.sleep(60)

