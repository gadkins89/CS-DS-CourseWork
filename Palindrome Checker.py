while True:


    print("""
    *******************************
    ****Palindrome Checker 9000****
    *******************************
    """)

    user_input = input("Please enter a word or phrase: \n").replace(" ", "")

    if user_input == user_input[::-1]:
        print(f"{user_input} is a palindrome. \n")
    else:
        print(f"{user_input} is not a palindrome. \n")

    user_quit_or_nah = input(str("Would you like to try again? (Y/N) \n")).lower()

    if user_quit_or_nah == "n":
        input("Press any key to exit. \n")
        break
    else:
        continue