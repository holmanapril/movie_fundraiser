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


# Main routine
user_age("How old are you?", "Please enter a valid age between(12 and 130)",
         "You are too young to be doing this")
