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
" Africa is where I fly, in open lands and desert sky. Slender build and darkened eye, I’m fierce and swift when prey is nigh. "
"what am i? ")
# Check if the password == 'Falcon'
    if agents_pasword == ("a falcon"):
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
    terminal_options = input("this terminal has only access to: []")
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