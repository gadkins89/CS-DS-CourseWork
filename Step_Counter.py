"""
6.20 LAB: Step counter

A pedometer treats walking 1 step as walking 2.5 feet. Define a function named feet_to_steps that takes
a float as a parameter, representing the number of feet walked, and returns an integer that represents 
the number of steps walked. Then, write a main program that reads the number of feet walked as an input, 
calls function feet_to_steps() with the input as an argument, and outputs the number of steps.

Use floating-point arithmetic to perform the conversion.
Ex: If the input is:
150.5

the output is:
60

The program must define and call the following function:
def feet_to_steps(user_feet)
"""

def feet_to_steps(user_feet):
    num_steps_walked = int(user_feet / 2.5)
    return num_steps_walked


if __name__ == "__main__":
    user_feet = float(input("Please enter the the footage you have walked today: \n"))

    print(f"Your current step count is: {feet_to_steps(user_feet)} \n")