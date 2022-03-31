# Functions
def name():
    valid = False
    # Keeps running loop until user inputs a valid name
    while not valid:
        # Asks them their name
        user_name = str(input("What is your name?")).title()
        # Checks if input is a number
        if user_name.isdigit():
            # If input is a number it prints error message
            print("Please enter a valid name")
        else:
            # Prints users name
            print(user_name)
            return user_name


# Main Routine
name()
