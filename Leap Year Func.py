# Define days in feb function.

def days_in_feb(user_year):
    is_a_leap_year = False

    if 0 == user_year % 4:
        if 0 == user_year % 100:
            if 0 == user_year % 400:
                is_a_leap_year = True
        else:
            is_a_leap_year = True

    if is_a_leap_year:
        print(f"{user_year} has 29 days in February. ")
    else:
        print(f"{user_year} has 28 days in February. ")

# Run main program.

if __name__ =="__main__":

    # Define year var and ask for input.

    year = int(input("Enter a year: "))

    # Call days in feb function using year var as function argument.

    days_in_feb(year)