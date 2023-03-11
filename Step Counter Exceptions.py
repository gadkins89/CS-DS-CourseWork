def steps_to_miles(num_steps):
    if num_steps < 0:
        print(f" {ValueError}: Exception: Negative step count entered. ")
    else:
        miles_walked = num_steps / 2000
        print(f"You walked {miles_walked:.2f} mile(s)!!! ")
        return miles_walked



if __name__ == "__main__":

    try:
        user_steps = int(input("Enter your step count: "))
    except ValueError as ve:
        print(f" ValueError: {ve} ")
   
    try:
        steps_to_miles(user_steps)
    except NameError as ne:
        print(f" NameError: {ne} ")