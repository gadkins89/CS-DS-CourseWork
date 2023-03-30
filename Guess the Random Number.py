import random

def number_guess(num):
    random_number = random.randint(1, 100)

    if random_number == num:
        print(f"{num}: Is Correct!!!")
    elif random_number > num:
        print(f"{num}: Is Too High!!! The correct number was: {random_number}. ")
    elif random_number < num:
        print(f"{num}: Is Too Low!!! The correct number was: {random_number}. ")
    
    return
    
        
if __name__ == "__main__":
    
    random.seed(900)
    
    
    user_input = input("Enter a list of integers between 1 and 100 separated by a space: \n")
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)