# kaginawa-payload-bme280-ccs811

[kaginawa](https://github.com/kaginawa/kaginawa) payload for bme280 + ccs811 sensing system.

## Prerequisites

Hardware:

- SMBus-compatible Linux-based platform (e.g. Raspberry Pi)
- BME280 with I2C slave address `0x76`
- CCS811 with I2C slave address `0x5b`

Software:

- [kaginawa](https://github.com/kaginawa/kaginawa)
- Python 3
    - smbus library (`pip3 install smbus` or `apt install python3-smbus`)

## Usage

`/etc/systemd/system/kaginawa-payload.service`:

```
[Unit]
Descriptiuon=kaginawa
After=network-online.target

[Service]
Type=simple
WorkingDirectory=/opt/kaginawa
ExecStart=/opt/kaginawa/main.py
Restart=always
User=kaginawa

[Install]
WantedBy=multi-user.target
```

Modify `ExecStart` as follows according to your configuration:

- BME280 + CCS811: `main.py`
- BME280 only: `main-bme280-only.py`
- CCS811 only: `main-ccs811-only.py`

systemd's registration:

```
sudo systemctl daemon-reload
sudo service kaginawa-payload start
sudo systemctl enable kaginawa-payload
```

`kaginawa.json`:

```json
{
  "server": "xxx.com",
  "api_key": "xxx",
  "custom_id": "xxx",
  "payload_command": "cat /opt/kaginawa/payload.json"
}
```

## Credits

`bme280.py` is based on [SWITCHSCIENCE/BME280](https://github.com/SWITCHSCIENCE/BME280), licensed under the MIT license.

`ccs811.py` is based on [adafruit/Adafruit_CCS811_python](https://github.com/adafruit/Adafruit_CCS811_python), licensed under the MIT License.

All programs are restyled with `pycodestyle`.

## License

[MIT License](LICENSE)

## Author

[mikan](https://github.com/mikan)
