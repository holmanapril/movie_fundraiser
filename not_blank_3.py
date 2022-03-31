# Functions
def not_blank(question, error):
    valid = False
    # Keeps running loop until user inputs a valid name
    while not valid:
        # Asks question
        user_name = str(input(question)).title()
        # Makes sure input isn't a number or blank
        if user_name.isnumeric() or user_name == "":
            # If digit or blank, error message prints
            print(error)
        else:
            print(user_name)
            return user_name


# Main Routine
# Runs not_blank function, with question and error parameters
not_blank("What is your name?", "Please enter a valid name")
