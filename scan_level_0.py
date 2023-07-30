#!/user/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=5)[0]
    print(answered_list.summary())

# scan(("192.168.0.1/24"))                    #defualt checkup IP
ip = input("Enter the IP or range: ")
scan(ip)