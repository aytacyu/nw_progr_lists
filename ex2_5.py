#!/usr/bin/env python
"""Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the
first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
"""
from __future__ import print_function, unicode_literals
with open("show_ip_bgp_summ.txt","r") as f:
    bgp_sum = f.readlines()
as_number = None
peer_ip = None
for line in bgp_sum:
    if "local AS number" in line:
        as_number = line.split()[-1]
    if line[0].isdigit() :
        peer_ip = line.split()[0]
print("Local AS Number: {}".format(as_number))
print("BGP Peer IP Address: {}".format(peer_ip))
