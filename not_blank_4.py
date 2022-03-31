# Functions
def not_blank(question, error):
    valid = False
    # Keeps running loop until user inputs a valid name
    while not valid:
        count = 0
        # Asks question
        user_name = str(input(question)).title().strip()
        for i in range(len(user_name)):
            if user_name[i].isspace():
                count += 1
        print(count)
        # Makes sure input isn't a number or blank
        if count >= 1:
            print(error)
        else:
            if user_name.isalpha() is False or user_name.isnumeric() or user_name == "":
                # If digit or blank, error message prints
                print(error)
            else:
                print(user_name)
                return user_name


# Main Routine
# Runs not_blank function, with question and error parameters
not_blank("What is your name?", "Please enter a valid full name(first and last name)")
