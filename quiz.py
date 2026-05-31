# name of the user saved in user-name #
print("what is your name user?")
user_name = input("")
# if user's name is dave. #
# an easter egg will trigger. #
if user_name == ("dave"):
# easter egg. #
    print("I'm sorry, "+ user_name + ". I'm afraid I can't do that.")
    print("but ill continue.")
# hidden question . #
    dactyl_question_one = input("dactyl is the moon of what. ")
    if dactyl_question_one == ("asteroid 243 Ida") or dactyl_question_one ==("an asteroid"):
        print("good job. test is now over")
    else:
        print("It can only be attributable to human error.")
# this is the introduction of quiz to the user. should the name value not be dave. #
# Moon_question_one is the variable that refers to the number of the question.  #
else:
    print("hello " + user_name + ". this is a quiz dedicated to the moons of this solar system. \n "
    "get atleast eleven points from correct answers and you'l get asci art as a reward."
    " i warn you. this is a hard one.")
    Moon_question_one = input("yes or no. have people truly been to the moon? ")
# the answer to the question correct or not is by the if and else statements #
    if Moon_question_one == "yes" or Moon_question_one == "no":
        print("sure sure buddy.")
    else:
        print("it Wasn't yes or no. so no point for you!!")

# the second question. functions the same as the first #
    Moon_question_Two = input("what is the name of the closest moon ")
    if Moon_question_Two == ("moon") or Moon_question_Two == ("luna"):
        print("yes!! point for you!! (i won't be counting tho)")
    else:
        print("the was wrong. minus one point.")

# and the third #
    Moon_question_Three = input("of what planet were the first moons discovered after the moon? ")
    if Moon_question_Three == ("saturn"):
        print("that correct!! that's three points? IDK")
    else:
        print("nope. minus one point for you!!. ")
    
    print("Good job so far " + user_name + " lets see if you get this one.")

# so is the fourth #
    Moon_question_four = input("how big is charon? ")
    if Moon_question_four == ("half the size of pluto"):
        print("that is correct!! add one more point.")
    else:
        print("should i dum these down for you? you loose one point more.")

# so is the fith #
    Moon_question_five = input("what are the names of the moons of mars? ")
    if Moon_question_five == "Phobos and Deimos" or Moon_question_five == "Deimos and Phobos":
        print("good. that is correct!! another point for you ")
    else:
        print("oops. that was wrong. maybe you spelt it wrong. minus one point for you i'm pretty sure you are in negtive points.")

    Moon_question_six = input("is eros a moon? ")
    if Moon_question_six == "its not a moon" or Moon_question_six == ("no"):
        Moon_question_seven = input("good job. in what year was eros discovered ")
        if Moon_question_seven == "1898":
            print("that is correct. plus one point")
        else:
            print("minus one point")
        
# true or false questions from here on. if answer is t or T. print correct. #
    Moon_question_eight_starter = input("want to switch it up? ")
    Moon_question_eight = input("At least 80 moons orbit the planet Jupiter. T or F \n i recommend you turn on CAPS. ")
    if Moon_question_eight_starter == ("ok") or Moon_question_eight_starter == ("yes") or Moon_question_eight_starter == ("yeah"):
        print("take one point off again.")
    
    elif Moon_question_eight == "T" or Moon_question_eight == "t":
        print("that is correct.! another point for you.")
    
    elif Moon_question_eight == ("f") or Moon_question_eight == ("F"):
        print("minus one point again.")

# so is the eighth #    
    Moon_question_nine = input("Mercury and Venus are the only two planets in our solar system that do not have moons. T or F ")
    if Moon_question_nine== "T" or Moon_question_eight == "T":
        print("that is correct.! another point for you.")
    else:
        print("minus one point again? this is getting repetitive.")

# so is the ninth #
    Moon_question_ten = input("" \
    "The footprints on the Moon from the NASA astronauts (circa Apollo 11) are expected to last for 100 million years. " \
    "T or F. ")
    if Moon_question_ten == "T" or Moon_question_ten == "t":
        print("corect again! one last question to go. plus one point.")
    else:
        print("minus one point again? this is getting repetitive.")

# so is the tenth #
    Moon_question_eleven = input("last one. We only ever see one side of the Moon. ")
    if Moon_question_eleven == "T" or Moon_question_eleven == "t":
        print("corect again! one last question to go. plus one point.")
    else:
        print("minus one point again? this is getting repetitive")

# so is the eleventh #
    Moon_question_twelve = input("The Moon has always looked the same size in the night sky. T or F ")
    if Moon_question_twelve == "F" or Moon_question_twelve == "f":
        print("corect again! one last question to go. plus one point.")
    else:
        print("minus one point again? this is getting repetitive")

# should the user get atleast 11 points. wt right. 
# this will trigger the print of a acai art #
reward_amount = input("this the real end of the quiz. Thank you for playing. \n" \
"just input the amount of points.\n it must be at least 11 " \
"and you'll recieve your complementary ASCII art. " + user_name + "\n " )





if not isinstance (int(reward_amount), int):
    print("write a number")
if  isinstance (int(reward_amount), int):
    print('''@  *  .  . *       *    .        .        .   *    ..
    @. /\ *     ###     .      .        .            *d
    @ /  \  *  #####   .     *      *        *    .
    ]/ [] \  ######### *    .  *       .  //    .  *   .
    / [][] \###\#|#/###   ..    *     .  //  *  .  ..  *
    |  __  | ###\|/###  *    *  ___o |==// .      *   *
    |  |!  |  # }|{  #         /\  \/  //|\
    |  ||  |    }|{    ejm97  / /        | \
                              ` `        '  '
    ''')

# if (reward_amount) >= 11:
#     print('''@  *  .  . *       *    .        .        .   *    ..
#     @. /\ *     ###     .      .        .            *
#     @ /  \  *  #####   .     *      *        *    .
#     ]/ [] \  ######### *    .  *       .  //    .  *   .
#     / [][] \###\#|#/###   ..    *     .  //  *  .  ..  *
#     |  __  | ###\|/###  *    *  ___o |==// .      *   *
#     |  |!  |  # }|{  #         /\  \/  //|\
#     |  ||  |    }|{    ejm97  / /        | \
#                               ` `        '  '
#     ''')
# elif (reward_amount) > 8 or (reward_amount) < 14:
#     print("no close enough. you got close tho. [KNOWLEDGE CHECK FINALIZED] ")

# else:
#     print("good bye. nice try. you finished the quiz.")

