""" Open the "show_version.txt" file for reading. Use the .read() method to read
in the entire file contents to a variable. Print out the file contents to the screen.
Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement).
Read in the file contents using the .readlines() method. Print out the file
contents to the screen. Also print out the type of the variable (you should
have a list at this point).
"""
from __future__ import print_function, unicode_literals
f=open("show_version.txt",'r')
output=f.read()
f.close()
print(output)
print("\n********************\n",type(output))

with open("show_version.txt") as f:
    lines=f.readlines()
print("\n********************\n",lines)
print("\n********************\n",type(lines))
