import sys

def title():
    #This function prints the game title.
    print("""
    **************************************
    ****Choose Your Own Adventure Game****
    **************************************
    **************The After***************
    **************************************
    """)

def opening_words():
    #This function prints the opening words to set the scene.
    print("""
    You find yourself in an post - apocalyptic wasteland. Grey skies
    filled with poison gasses and nuclear fallout loom as you spend 
    your days trying to find supplies to sustain. You are searching for
    medicine in an old drugstore when you notice an odd spot on the floor. 
    You inspect further and find an entrance to an underground opening.
    """)

def game_over():
    #This function exits the game.
    print("Goodbye. \n")
    input("Press any key to exit. \n")
    sys.exit ("")


def player_ready():
    #This function goes through the initial player ready setup.
    while True:
        ready_to_play = input("Are you ready for an adventure? (Y/N) \n").lower()
        if ready_to_play == "y":
            print("Let's Go! \n ")
            input("Press any key to begin. \n ")
            break
        elif ready_to_play == "n":
            print("Why are you here!? Come back when you are ready! \n")
            leave = input("Would you like to exit the game? (Y/N) \n").lower()
            if leave == "y":
                game_over()
            if leave == "n":
                print("Let us try again! ")          
        else:
            input("You entered an invalid command! Press any key to continue. ").lower()
        continue   


#Opening


title()

player_ready()    


# Game Start


opening_words()


while True:
                      
    
    drugstore = input("""
    a) Enter the Opening
    b) Leave the Drugstore
    c) Seal the opening
    """).lower()


# Starting Option a


    if drugstore == "a":
        print("You find yourself in an underground tunnel and spot a flickering light ahead. ")
        tunnel = input("""
    a) Follow the Light
    b) Leave the Tunnel
    """).lower()
        
        if tunnel == "a":
            print("The light becomes brighter as you come to a tee in the tunnel system. ")
            tunnel_turn = input("""
    a) Turn Right
    b) Turn Left
    """).lower()

        if tunnel == "b":
            print("""
    You leave the tunnel and pretend the light you saw didn't exist.
    Curiosity killed the cat, right??
    """)
        try_again = input("Would you like to try again? (Y/N) \n").lower()
            
        if try_again == "n":
            game_over()
            
        elif try_again == "y":
            continue
            
        if tunnel_turn == "b":
            print("A few hundred yards down the tunnel you fall into a cavern.")
            
            try_again = input("Would you like to try again? (Y/N) \n").lower()
            
            if try_again == "n":
                game_over()
                
            elif try_again == "y":
                continue
               
        if tunnel_turn == "a":
            print("""
    You see a group of people and they seem to be happy,
    healthy, and well fed.
    """)
            engage_people = input("""
    a) Engage the Group of People
    b) Run Away
    """).lower()

            if engage_people == "a":
                    print("""
    The group introduces themselves and accepts you with open arms. You know you will
    never have to be alone again. You live happily ever after.
    """)
                    try_again = input("Would you like to try again? (Y/N) \n").lower()
            
                    if try_again == "n":
                        game_over()
                        
                    elif try_again == "y":
                        continue
                    
            if engage_people == "b":
                    print("""
    You run back down the tunnel and make it out alive. You never return and wonder
    if you made the right decision for the rest of your days.
    """)
                    try_again = input("Would you like to try again? (Y/N) \n").lower()
            
                    if try_again == "n":
                        game_over()
                        
                    elif try_again == "y":
                        continue
                
                                
#Starting Option b


    if drugstore == "b":
        print("""
    As you leave the drugstore you hear a pack of rabid bunnies closing in fast. You
    run back inside the drugstore and close the door. You know the door won't hold
    for long so you run out the back into the alley.
    """)
        climb_run = input("""
    a) Climb the ladder to the top of the drugstore
    b) Run down the alley to seek a better shelter
    """).lower()

        if climb_run == "a":
            print("""
    You arrive at the top of the building just in time to see a helicopter off in
    the distance.
    """)
            helicopter = input("""
    a) Light a flare to alert the helicopter
    b) Hide from the helicopter
    """).lower()

        if climb_run == "b":
            print("""
    You run down the ally and step in a bear trap. You are attacked by the rabid bunnies
    which is simultaneously the cutest / scariest thing to ever happen in your life.
    """)
            try_again = input("Would you like to try again? (Y/N) \n").lower()
            
            if try_again == "n":
                game_over()
                
            elif try_again == "y":
                continue
            
        if helicopter == "a":
            print("""
    The helicopter lands on top of the drugstore and you spot a familiar face. The pilot
    is one of your old friends from the Marine Corps. He welcomes you into the helicopter
    and you fly to safety and live happily ever after.
    """)
            try_again = input("Would you like to try again? (Y/N) \n").lower()
            
            if try_again == "n":
                game_over()
                
            elif try_again == "y":
                continue
            
        if helicopter == "b":
            print("""
    While making a mad run for cover you slide off the roof and fall to your demise.
        """)
            try_again = input("Would you like to try again? (Y/N) \n").lower()
            
            if try_again == "n":
                game_over()
                
            elif try_again == "y":
                continue
            
            
    #Starting Option c


    if drugstore == "c":
        print("""
    While trying to seal the opening with a heavy stone you uncover what seems to
    be a weathered map of sorts.
    """)
        examine_map = input("""
        A) Examine the map
        B) Continue about your business
        """).lower()

        if examine_map == "a":
            print("The map shows a route to a hidden spot in the bay. ")
            follow_map = input("""
            A) Follow the map
            B) Use the map as kindling for the evening fire
            """).lower()

            if follow_map == "a":
                print("""
                You follow the map through a winding trail well hidden in the bush. When
                you make it to the bay you find an alomost perfectly hidden pontoon boat.
                """)
                all_aboard = input("""
                A) Board the boat and check things out
                B) Sink the boat
                """).lower()

                if all_aboard == "a":
                    print("""
                    You find a pre-programmed GPS. The GPS leads you to a small island
                    with an underground bunker. There is a good 25 years worth of MRE's,
                    an advanced water filtration system, a bio-fuel refining system
                    to keep the boat running, and many other supplies. You give thanks to
                    the Lord and enjoy your abundant gifts for the rest of your days.
                    """)
                    try_again = input("Would you like to try again? (Y/N) \n").lower()
            
                    if try_again == "n":
                        game_over()
                    
                    elif try_again == "y":
                        continue
                
                elif all_aboard == "b":
                    print("""
                    After sinking the boat you decide to stay on the coast. You end up drinking
                    dirty water and find your way into the next world via dysentery.
                    """)
                    try_again = input("Would you like to try again? (Y/N) \n").lower()
            
                    if try_again == "n":
                        game_over()
                    
                    elif try_again == "y":
                        continue

            elif follow_map == "b":
                print("""
                A giant mutated penguin is attracted to your camp due
                to the savory smell of burning map. The penguin makes you his evening meal, curls
                up next to your fire, and has sweet, sweet giant mutated penguin dreams about the
                mysteries of the celestial bodies orbiting his once vibrant planet.
                """)
                try_again = input("Would you like to try again? (Y/N) \n").lower()
            
                if try_again == "n":
                    game_over()
            
                elif try_again == "y":
                    continue
        
        elif examine_map =="b":
            print("""
            While in denial of spotting a perfectly good map, you lose your footing
            and take a piece of rusty rebar through the thigh. Infection sets in and
            you are pushing daisies before the end of the week.
            """)
            try_again = input("Would you like to try again? (Y/N) \n").lower()
            
            if try_again == "n":
                game_over()
            
            elif try_again == "y":
                continue