import random

class GVDie:  
   def __init__(self):      
      # set default values
      self.my_value = random.randint(1, 6)
      self.rand = random.Random()

   def roll(self):
       self.my_value = self.rand.randint(1, 6)  
      
   # set the random number generator seed for testing
   def set_seed(self, seed):
       self.rand.seed(seed)
   
   # allows dice to be compared if necessary
   def compare_to(self, other):
       return self.my_value - die.my_value
       

def roll_total(die, total): 
    tot_val = 0
    tot_roll = 0
    while tot_val < total:
        die.roll()
        tot_val += die.my_value
        tot_roll += 1
    return tot_roll


if __name__ == "__main__":
    die = GVDie()   # Create a GVDie object
    die.set_seed(15)   # Set the GVDie object with seed value 15
          
    total = int(input("Enter a number: \n"))
    rolls = roll_total(die, total) # Should return the number of rolls to reach total.
    print(f'Number of rolls to reach at least {total}: {rolls}')