#!/usr/bin/env python
"""Exercises using Netmiko"""
import os
from getpass import getpass
from netmiko import ConnectHandler


def save_file(filename, show_run):
    """Save the show run to a file"""
    with open(filename, "w") as f:
        f.write(show_run)


def main():
    """Exercises using Netmiko"""

    # For automated testing
    sros_password = os.getenv("SROS_PASSWORD")
    if sros_password is None:
        sros_password = getpass("Enter SROS password: ")

    vmx_password = os.getenv("JNPR_PASSWORD")
    if vmx_password is None:
        vmx_password = getpass("Enter vMX password: ")

    sros1 = {
        "device_type": "nokia_sros",
        "host": "sros.lasthop.io",
        "username": "admin",
        "password": sros_password,
        "port": 2211,
    }

    vmx1 = {
        "device_type": "juniper_junos",
        "host": "vmx1.lasthop.io",
        "username": "pyclass",
        "password": vmx_password,
    }

    for a_device in (sros1, vmx1):
        net_connect = ConnectHandler(**a_device)
        print("Current Prompt: " + net_connect.find_prompt())

        show_ver = net_connect.send_command("show version")
        print()
        print("#" * 80)
        print(show_ver)
        print("#" * 80)
        print()

        if "sros" in a_device["device_type"]:
            cmd = "admin display-config"
        elif "juniper" in a_device["device_type"]:
            cmd = "show configuration"

        show_run = net_connect.send_command(cmd)
        filename = net_connect.base_prompt + ".txt"
        print("Save show run output: {}\n".format(filename))
        save_file(filename, show_run)


if __name__ == "__main__":
    main()
