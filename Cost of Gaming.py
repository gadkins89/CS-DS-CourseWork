# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:13:25 2022

@author: greya
"""

#Ask user how many snacks they eat per hour

snacks_per_hour= float(input("How many snacks per hour do you eat? "))

print (f"You entered {snacks_per_hour} snacks per hour. ")


#How many hours do they game

hours_per_game= float(input("How many hours do you game? "))

print (f"You entered {hours_per_game} hours. ")


#How much do they pay per snack

dollars_per_snack= float(input("How much do your snacks cost? "))

print (f"You entered ", end = "") 

print ('${:.2f}'.format(dollars_per_snack), end = "")

print (" per snack. ")

dollars_per_game= snacks_per_hour*hours_per_game*dollars_per_snack

print (f"Your total cost per gaming session is ", end = "") 

print ('${:.2f}'.format(dollars_per_game), end = "")

print (" . ")