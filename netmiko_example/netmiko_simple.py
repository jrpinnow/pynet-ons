#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

device = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": password,
    "port": 2211,
}

# Will automatically 'disconnect()'
with ConnectHandler(**device) as net_connect:
    print(net_connect.find_prompt())
