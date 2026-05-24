### Secret Agent Login
# Create a login process for a secret agent
login = "lorem ipsum"
# Ask for the user's name and save it in a variable
                    #greetings user. insert you code name.#
users_name = input (".eman edoc uoy tresni .resu sgniteerg ")
if users_name == "bond" or users_name == "james" or users_name == "james bond" or users_name == "ethan hunt":
# Ask for the password and save it in a variable
    agents_pasword = input("wellcome agent " + users_name + " good to see you again. just to comfirm that you are you. "
"answer this ridle please. it will reveal the pass-code."
" Africa is where I fly, in open lands and desert sky.\n"
" Slender build and darkened eye, I’m fierce and swift when prey is nigh. "
"what am i? ")
# Check if the password == 'Falcon'
    if agents_pasword == ("a falcon") or agents_pasword == ("falcon"):
    # Ouput that access has been granted and welcome user using their name
        print("yes. it is truely you. "+ users_name +" welcome to the terinal. a few more segurity to go throught. ")
    else:
        print("[LIFE PRIVILEGES REVOKED. NOW RELEASING POISON GAS] SssSssSssss")

    # Ask for the user's age and save it in a variable
    users_age = int( input("what is your age. agent. "))
    # Change the age into an integer

    # If the user's age is under 13, tell them they are a spy in training
    if users_age < 13:
        print("you are no agent. merely in training. sending head quarters your location and notifiing them to update the segurity.  you are unathorized.")

    # If their age is under 18, tell them they are a junior spy
    elif users_age < 18:
        print("you are a junior agent. you are you are unathorized.")

    # If their age is 18 or over, tell them they are a Field Agent
    else:
        print("you are a field agent. you are athorized.")
    terminal_options = input("this terminal has analyzed you clearance level and with grant you only access to: "
    "[ the truth of the Washington Monument ]\n" \
    "[ the truth about abe lincoln ]\n" \
    "[ what cartoons is short for  ]\n" \
    "[ how to defeat the british ]\n" \
    "\n" \
    "type Washington Monument or abe lincoln or what cartoons is short for to access.\n"
    "\n"
    " ")
    while terminal_options == "Y":
    
        terminal_options = input("want to go back to terminal options? type Y")
        if terminal_options == ("Washington Monument") or terminal_options == ("the truth of the Washington Monument") :
            print("the Washington Monument is the horn of what remains of THE LINCLOPS." \
            "The massive bellowing Cyclops that Lincoln rode into battle to win the Civil war. ")

        elif terminal_options == ("the truth about abe lincoln") or terminal_options == ("abe lincoln"):
            print("Abraham Lincoln wore that hat so nobody could see [CLASSIFIED] sitting on his head, pulling his hair, and controling his body. ")
            print(terminal_options)
        

    
        elif terminal_options == ("what cartoons is short for"):
            print("They were called ""cartoons,"" short for carcinogenic toons, since they were painted on cancer-causing celluloid. ")

    
        elif terminal_options == ("how to defeat the british"):
            print("Simply destroy their tea, the secret to their power! (British blood is 80% tea--throwing away tea in front of them is like shooting a werewolf with a silver bullet). ")
       
    
        else:
            print("that is not available.")
      
else:
    print("you are not a real spy." \
    " you may leave this terminal immediately ")
# Output a goodbye

# ___________________________

# EXTENSION

# Ask more questions to give your spy more information
# Look up how to use 'and' and 'or' to force more conditions (eg. they must be one of 3 users AND get the password correct)

# ___________________________

# EXPERT (For those who already know python)

# Create a SPY ID GENERATOR
# Your user must login using the correct password to access the generator
# Use a bunch of questions to generate an id. Eg. If their name has 4 or fewer letters, their ID is a random fruit plus other logic...