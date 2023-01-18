# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 22:01:50 2022

@author: greya
"""

"""
Driving is expensive. Write a program with a car's miles/gallon and gas dollars/gallon (both floats) as input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3))

Ex: If the input is:

20.0
3.1599
Then the output is:

3.16 11.85 79.00
"""

car_miles_per_gallon = float(input("Please enter your car miles per gallon: "))
print(f"You entered {car_miles_per_gallon} miles per gallon. ")

gas_price_per_gallon = float(input("Please enter the price of gas per gallon: "))
print(f"You entered ", end = "")
print("$" + format(gas_price_per_gallon, ",.2f"), end = "")
print(" per gallon.")

cost_for_20_mile_trip = (20.0 / car_miles_per_gallon) * gas_price_per_gallon
cost_for_75_mile_trip = (75.0 / car_miles_per_gallon) * gas_price_per_gallon
cost_for_500_mile_trip = (500.0 / car_miles_per_gallon) * gas_price_per_gallon

print('Your cost for a 20, 75, and 500 mile trip is ${:.2f} ${:.2f} ${:.2f}, respectively. '.format(cost_for_20_mile_trip, cost_for_75_mile_trip, cost_for_500_mile_trip))