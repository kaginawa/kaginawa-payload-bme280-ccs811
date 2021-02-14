# kaginawa-payload-bme280-ccs811

[kaginawa](https://github.com/kaginawa/kaginawa) payload for bme280 + ccs811 sensing system.

## Prerequisites

Hardware:

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
WorkingDirectory=/home/pi/kaginawa
ExecStart=/home/pi/kaginawa/main.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

systemd registration:

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

`ccs811.py` is based on [adafruit/Adafruit_CCS811_python](https://github.com/adafruit/Adafruit_CCS811_python), licensed under the MIT License.

`bme280.py` is based on [SWITCHSCIENCE/BME280](https://github.com/SWITCHSCIENCE/BME280), licensed under the MIT license.

All programs are restyled with `pycodestyle`.

## License

[MIT License](LICENSE)

## Author

[mikan](https://github.com/mikan)

