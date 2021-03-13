#! /bin/python3

# Run this with root privileges

import scapy.all as sc


def scan(ip):
    sc.arping(ip)


scan("10.0.0.2/24")
