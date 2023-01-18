# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 22:05:04 2022

@author: greya
"""

number_1 = float(input("Please enter a number. "))
print(f"You entered {(number_1):.2f}. ")

number_2 = float(input("Please enter a second number. "))
print(f"You entered {(number_2):.2f}. ")

number_3 = float(input("Please enter a third number. "))
print(f"You entered {(number_3):.2f}. ")

number_4 = float(input("Please enter a fourth number. "))
print(f"You entered {(number_4):.2f}. ")

print(f"The rounded product of these numbers is equal to {(number_1*number_2*number_3*number_4):.0f} ")

print(f"The rounded average of these numbers is equal to {((number_1+number_2+number_3+number_4)/4):.0f} ")

print(f"The float product of these numbers is equal to {(number_1*number_2*number_3*number_4):.3f} ")

print(f"The float average of these numbers is equal to {((number_1+number_2+number_3+number_4)/4):.3f} ")


