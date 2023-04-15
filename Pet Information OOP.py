"""
13.7 LAB: Pet information (derived classes)
The base class Pet has attributes name and age.
The derived class Cat inherits attributes from the base class
(Pet) and includes a breed attribute. Complete the program to:

Create a generic pet, and print the pet's information using print_info().
Create a Cat pet, use print_info() to print the cat's information, and add
a statement to print the cat's breed attribute.
"""


#Starter Code

class Pet:
    def __init__(self):
        self.name = ''
        self.age = int()
        self.species = ''
        self.breed = ''

    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: { self.name }')
        print(f'   Age: { self.age }')
        return


class Cat(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.breed = ''

    def print_info(self):
        Pet.print_info(self)
        print(f'   Breed: {self.breed }')
        return
        
        

if __name__ == "__main__":

    my_pet = Pet()
    my_cat = Cat()

    my_pet.name = input("Enter your pet's name: \n")
    my_pet.age = int(input("Enter your pet's age: \n"))

  
    my_cat.name = input("Enter your cat's name: \n")
    my_cat.age = int(input("Enter your cat's age: \n"))
    my_cat.breed = input("Enter the breed of your cat: \n")

    

    my_pet.print_info()
    my_cat.print_info()