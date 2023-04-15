'''
13.11 LAB: Plant information
Given a base Plant class and a derived Flower class, write a program to
create a list called my_garden. Store objects that belong to the Plant class
or the Flower class in the list. Create a function called print_list(), that
uses the print_info() instance methods defined in the respective classes and
prints each element in my_garden. The program should read plants or flowers
from input (ending with -1), add each Plant or Flower to the my_garden list,
and output each element in my_garden using the print_info() function.

Note: A list can contain different data types and also different objects.

Ex. If the input is:

plant Spirea 10 
flower Hydrangea 30 false lilac 
flower Rose 6 false white
plant Mint 4
-1
the output is:

Plant Information: 
   Plant name: Spirea
   Cost: 10

Plant Information: 
   Plant name: Hydrangea
   Cost: 30
   Annual: false
   Color of flowers: lilac

Plant Information: 
   Plant name: Rose
   Cost: 6
   Annual: false
   Color of flowers: white

Plant Information: 
   Plant name: Mint
   Cost: 4
'''


# Starter Code

class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')

class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')
        print(f'   Annual: { self.is_annual }')
        print(f'   Color of flowers: { self.color_of_flowers }')

def print_list(my_garden):
    print("Plant Information: \n")
    for plant in my_garden:
        plant.print_info()

# TODO:  Define the print_list() function that prints a list of plant (or flower) objects 

if __name__ == "__main__":

    my_garden = []

    # TODO: Declare a list called my_garden that can hold object of type plant

    user_string = input('''
===============================================================
===================GARDEN BUILDER 9000=========================
===============================================================
|If you are entering a plant,                                 |
|enter the plant information in the following format:         |
|Plant, Plant Name, Plant Cost (Omit the Commas)              |
===============================================================
|If you are entering a flower,                                |
|enter the flower information in the following format:        |
|Flower, Flower Name, Flower Cost, Is Annual (True or False), |
|Color of Flowers (Omit the Commas)                           |
===============================================================
|Enter as many plants as you wish in order to build your      |
|garden. Enter bye to print out your garden.                  |
===============================================================
    \n''').lower()
    
    while user_string != "bye":
        lst = user_string.split(" ")
        if lst[0] == "plant":
            my_garden.append(Plant(lst[1], float(lst[2])))
        elif lst[0] == "flower":
            my_garden.append(Flower(lst[1], float(lst[2]), bool(lst[3]), lst[4]))
            
        #else:
            #if user_string[0] == "bye":
                #break
 
        # TODO: Check if input is a plant or flower
        #       Split the user_string input into variables - plant_name, plant_cost, color_of_flowers, is_annual
        #       Store as a plant object or flower object
        #       Add to the list my_garden
        user_string = input("\n")

    print_list(my_garden)

    # TODO: Call the print_list() function to print my_garden