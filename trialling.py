# Functions
def user_age(question, error, error_2):
    valid = False
    # Continues to ask for input until valid input it entered
    while not valid:
        try:
            # Asks for age
            age = int(input(question))
            if age <= 11:
                # If too young, code will finish
                print(error_2)
                return age
            elif age >= 131:
                # If too old, user will be re-asked
                print(error)
            else:
                # If valid age, code finishes
                print(age)
                return age
        except ValueError:
            # Prints error message if string is input
            print(error)


def not_blank(question, error):
    valid = False
    # Asks user what their name is
    print(question)
    # Keeps asking user what their name is until they enter a valid name
    while not valid:
        # Gets users input and stores it as user_name
        user_name = str(input()).title().strip()
        # Counts the amount of spaces in users name after strip()
        spaces = (user_name.count(" "))
        # Replaces space with no space so the next code works
        user_name_no_space = user_name.replace(" ", "")
        # Checks if user_name is all letter and isn't blank
        if user_name_no_space.isalpha() is False or user_name_no_space == "":
            # If user_name is not all letter or is blank, error message is printed
            print(error)
        else:
            # Once the rest of the if is passed it comes to check if the amount of spaces is more than 0
            if spaces >= 1:
                # If spaces is more than 0, it reprints name and ends the function
                print(user_name)
                return user_name
            else:
                # If spaces = equal 0, it prints error and then asks for input again
                print(error)


# Main Routine
not_blank("What is your name?", "Please enter a valid full name(first and last name)")
user_age("How old are you?", "Please enter a valid age(12-130)",
         "You are too young to be doing this")
