# Define max magnitude function.

def max_magnitude(user_val1, user_val2, user_val3):
    if user_val1 < 0 or user_val2 < 0 or user_val3 < 0:
        max_mag_neg = min(user_val1, user_val2, user_val3)
        print(max_mag_neg)
    else:
        max_mag = max(user_val1, user_val2, user_val3)
        print(max_mag)

# Run main program.


if __name__ == "__main__":

    # Assign variables and request input.

    val1 = int(input("Please enter a number: "))
    val2 = int(input("Please enter another number: "))
    val3 = int(input("Please enter a final number: "))

    # Call max magnitude function using val1, val2, and val3 for arguments.

    max_magnitude(val1, val2, val3)