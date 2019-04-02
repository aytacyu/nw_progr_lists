""". Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:
from pprint import pprint
pprint(some_var)
Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt"
"""
from pprint import pprint
with open("show_arp.txt","r") as f:
    lines=f.readlines()[1:]
pprint(lines)
lines.sort()
new_list = lines[:3]
new_list = "\n".join(new_list)
pprint(new_list)

with open("arp_entries.txt","w") as f:
    f.write(new_list)

