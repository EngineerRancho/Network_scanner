#!/user/bin/env python

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

ip = input("Enter the IP or range: ")
scan(ip)