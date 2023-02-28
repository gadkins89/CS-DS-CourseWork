from random import randint


class RandomNumbers:
    def __init__(self):
        self.get_var1 = 0
        self.get_var2 = 0
        self.get_var3 = 0

    def set_random_values(self, low, high):
        self.var1 = randint(low, high)
        self.var2 = randint(low, high)
        self.var3 = randint(low, high)
        return self.var1, self.var2, self.var3
    
    def get_random_values(self):
        print(f"Random values: {self.var1} {self.var2} {self.var3} ")
        
    

if __name__ == "__main__":
    
    low = int(input("Enter a low number: \n"))
    high = int(input("Enter a high number: \n"))

    numbers = RandomNumbers()

    numbers.set_random_values(low, high)

    numbers.get_random_values()