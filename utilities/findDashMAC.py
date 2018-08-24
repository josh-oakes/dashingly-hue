#!/usr/bin/env python

from scapy.all import *


def arp_display(pkt):
    if scapy.all.ARP in pkt and pkt[scapy.all.ARP].op in (1, 2):  # who-has or is-at
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")


print(scapy.all.sniff(prn=arp_display, filter="arp", store=0, count=0))