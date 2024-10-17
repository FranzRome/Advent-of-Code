"""
--- Day 16: Ticket Translation ---
"""

import os


import input_reader 

input_reader.read_tickets_file()

print(os.path.dirname(__file__))

f = open(".//inputs//day16.txt", "r")
print(f.read()) 