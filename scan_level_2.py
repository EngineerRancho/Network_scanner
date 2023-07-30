#!/user/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=5)
    print(answered.summary)
    # arp_request.show()
    # broadcast.show()
    # scapy.ls(scapy.Ether())
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    # scapy.arping(ip)

ip = input("Enter the IP or range: ")
scan(ip)