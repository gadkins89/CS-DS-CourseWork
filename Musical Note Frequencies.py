# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 22:06:21 2022

@author: greya
"""

"""
On a piano, a key has a frequency, say f0. Each higher key (black or white) has a frequency of f0 * r^n, where n is the distance (number of keys) from that key, and r is 2^(1/12). Given an initial key frequency, output that frequency and the next 4 higher key frequencies.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4, your_value5))

Ex: If the input is:

440
(which is the A key near the middle of a piano keyboard), the output is:

440.00 466.16 493.88 523.25 554.37
Note: Use one statement to compute r = 2^(1/12) using the pow function (remember to import the math module). Then use that r in subsequent statements that use the formula fn = f0 * r^n with n being 1, 2, 3, and finally 4.
"""

base_frequency = float(input("What is your base frequency? "))

print (f"You entered {base_frequency} as your base frequency. ")

import math
r = math.pow(2.0, (1.0/12.0))
print (f"r has the value of {r}.")

one_key_up = base_frequency * (math.pow(r, 1))
two_keys_up = base_frequency * (math.pow(r, 2))
three_keys_up = base_frequency * (math.pow(r, 3))
four_keys_up = base_frequency * (math.pow(r, 4))

print('Your base frequency is: {:.2f} One key up is: {:.2f} Two keys up is: {:.2f} Three keys up is: {:.2f} Four keys up is: {:.2f}'.format(base_frequency, one_key_up, two_keys_up, three_keys_up, four_keys_up))


       
       
