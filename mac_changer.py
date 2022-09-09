#!/usr/bin/env python
from ast import arguments
import re
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest= "interface", help="Interface to change MAC Direction")
    parser.add_option("-m", "--mac", dest= "new_mac", help="New MAC Direction")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error("[-] Please add a available interface, use --help to more information")
    elif not options.new_mac:
        parser.error("[-] Please add a available MAC Direction, use --help to more information")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC Direction to " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_MAC(interface):
    ifconfig_results = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Error to get the MAC Direction")

options = get_arguments()
current_mac = get_current_MAC(options.interface)
print("Current MAC: " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_MAC(options.interface)

if current_mac == options.new_mac:
    print("[+] MAC Direction has change correctly to " + current_mac)
else:
    print("[-] MAC Direction hasn't change")

