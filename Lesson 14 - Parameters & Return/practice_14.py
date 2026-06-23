"""
PROGRAM: Geometry Helper
This program helps to calculate the area and perimeter of a rectangle
"""

####### INSTRUCTIONS ########
# Complete the code by writing functions for calculating the area and perimeter 
# taking the user input and returning it, 
# and calling each function based on user choice


# =====================================================================
# FUNCTIONS
# =====================================================================

# TODO ------->>>> Write a function here for calculating the area of a rectangle using passed values. 
def calculate_areof_rectangle():
    area = width_input * length_input
    width_input = int(input("to calculate the area of your rectange." \
    "please provide the width of this rectangle."))
    if width_input == int:
        print("thank you.")
    elif width_input == float:
        print("thank you.")
    else:
        print("the width value you inputed is not a number.")
    length_input = int(input("now input the length of the rectangle"))
    if length_input == int:
        print ("thank you")
    elif length_input == float:
        print("thank you.")
    else:
        print("that is not a number")
    return area
calculate_areof_rectangle()
# TODO ------->>>> Return the result.


# TODO ------->>>> Write a function here for calculating the perimeter using passed values. 
# TODO ------->>>> Return the result.

def display_result(message):
    print("\n------------------")
    print(message)
    print("------------------")

# Run the main program
def main():

    print("Welcome to the Geometry Helper for rectangles!\n")
    print("1. Area Calculator")
    print("2. Perimeter Calculator")

    length = int(input("What is the length of your rectangle?").strip())
    width = int(input("What is the width of your rectangle?").strip())

    choice = input("\nWhich tool do you want to use? (1 or 2): ").strip()

    # Trigger function based on user choice
    if choice == "1":
        
        # TODO ------->>>> Call the function for calculating area here and save it into variable 'area'

        display_result(f"The area of your rectangle is {area}².")

    elif choice == "2":

        # TODO ------->>>> Call the function for calculating perimeter here and save it into variable 'perimeter'

        display_result(f"The perimeter of your rectangle is {perimeter}.")

    else:
        print("Invalid choice. Exiting dashboard.")


# =====================================================================
# EXECUTION
# =====================================================================

main()