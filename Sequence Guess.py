#  Write a program that gives the first five terms of a sequence
#  and asks the user to guess the sixth. The program should be able
#  to choose between four sequences.

import random

sequences = ["sequence_one", "sequence_two", "sequence_three", "sequence_four"]

ones = [0, 1, 2, 3, 4]
twos = [0, 2, 4, 6, 8]
squares = [2, 4, 16, 256, 65536]
fun = [0, 1, 3, 7, 15]


def sequence_one():
    
    print(f"Sequence number one is: {ones} \n")

    user_guess = int(input("Can you guess the next number in this sequence? \n"))

    correct_guess = ones[-1] + ones[1]
    
    if user_guess == correct_guess:
        print("That is correct! \n")
    else:
        print("You are mistaken. \n")
    
    return



def sequence_two():
    
    print(f"Sequence number two is: {twos} \n")

    user_guess = int(input("Can you guess the next number in this sequence? \n"))

    correct_guess = twos[-1] + twos[1]
    
    if user_guess == correct_guess:
        print("That is correct! \n")
    else:
        print("You are mistaken. \n")
    
    return


def sequence_three():
    
    print(f"Sequence number two is: {squares} \n")

    user_guess = int(input("Can you guess the next number in this sequence? \n"))

    correct_guess = squares[-1] ** 2
    
    if user_guess == correct_guess:
        print("That is correct! \n")
    else:
        print("You are mistaken. \n")
    
    return


def sequence_four():
    
    print(f"Sequence number two is: {fun} \n")

    user_guess = int(input("Can you guess the next number in this sequence? \n"))

    correct_guess = (fun[-1] * 2) + 1
    
    if user_guess == correct_guess:
        print("That is correct! \n")
    else:
        print("You are mistaken. \n")
    
    return

def sequence_generator():
    random_sequence = random.choice(sequences)

    if random_sequence == "sequence_one":
        sequence_one()
    elif random_sequence == "sequence_two":
        sequence_two()
    elif random_sequence == "sequence_three":
        sequence_three()
    elif random_sequence == "sequence_four":
        sequence_four()


if __name__ == "__main__":

    sequence_generator()