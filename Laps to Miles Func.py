# Define laps to miles function.

def laps_to_miles(num_laps):
    miles = float(num_laps) * (0.25)
    format_miles = "{:.2f}".format(miles)
    print(f"You traveled {format_miles} miles. ")
    return

# Run main program.

if __name__ == "__main__":

    # Define laps var and ask for user input.

    laps = input("Enter the number of laps: ")

    # Convert laps var to float.

    float(laps)

    # Call laps to miles function using laps var as function argument.

    laps_to_miles(laps)