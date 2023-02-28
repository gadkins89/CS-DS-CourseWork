import random

class GVDie:  
   def __init__(self):      
      self.my_value = random.randint(1, 6)
      self.rand = random.Random()

   def roll(self):
       self.my_value = self.rand.randint(1, 6)  
      
   def set_seed(self, seed):
       self.rand.seed(seed)
   
   def compare_to(self, other):
       return self.my_value - die.my_value
       

def roll_specific_number(die, num, goal):
    rolls = 0
    count = 0

    while count < goal:
        die.roll()
        if die.my_value == num:
            count += 1
        rolls += 1
    return rolls



if __name__ == "__main__":
    die = GVDie()
    die.set_seed(15)
          
    num = int(input("Enter the number you would like to roll: \n"))
    goal = int(input("Enter the amount of times you would like to roll your number: \n"))
    rolls = roll_specific_number(die, num, goal)
    print(f'It took {rolls} rolls to get a \"{num}\" {goal} times.')