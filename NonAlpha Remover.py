while True:


    print("""
    ****************************************
    ****Non-Alpha Character Remover 9000****
    ****************************************
    """)

    user_input = input("Please enter.... Well, enter anything: \n")

    clean_user_input = "".join(filter(str.isalnum, user_input))

    print(clean_user_input)

    user_quit_or_nah = input("Would you like to try again? (Y/N) \n").lower()

    if user_quit_or_nah == "n":
        input("Press any key to exit. \n")
        break
    else:
        continue