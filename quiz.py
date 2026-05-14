# obtains the name of the user. then if the user's name happens to be or inputs dave. the name dave will trigger a line of easter egg questions. if the name is anything but dave. #
# the program will use the regular questions #
print("what is your name user?")
user_name = input("")
if user_name == ("dave"):
    print("I'm sorry, Dave. I'm afraid I can't do that.")
    print("but ill continue.")
    dactyl_question_one = input("dactyl is the moon of what.")
    if dactyl_question_one == ("asteroid 243 Ida") or dactyl_question_one ==("an asteroid"):
        print("good job. test is now over")
    else:
        print("It can only be attributable to human error.")
# this is the introduction of quiz to the user. should the name value not be dave. #
# Moon_question_one is the variable that refers to the number of the question.  #
else:
    print("hello " + user_name + ". this is a quiz dedicated to the moons of this solar system. get all the answers correct and you'l get acaii art as a reward")
    Moon_question_one = input("yes or no. have people truly been to the moon? ")
# the answer to the question correct or not is by the if and else statements #
    if Moon_question_one == "yes":
        print("sure sure buddy.")
    else:
        print("sure sure buddy.")

# the second question. functions the same as the first #
    Moon_question_Two = input("what is the name of the closest moon ")
    if Moon_question_Two == "moon":
        print("yes!! point for you!! (i won't be counting tho)")

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
        print("oops. that was wrong. minus one point for you> i'm pretty sure you are in negtive points.")

    Moon_question_five = input("is eros a moon?")
    if Moon_question_five == "not its not a moon":
        input("good job. what happened to eros?")

