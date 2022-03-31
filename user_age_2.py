valid = False
# Continues to ask for input until valid input it entered
while not valid:
    try:
        # Asks for age
        age = int(input("How old are you?"))
        if age <= 11:
            # If too young, code will finish
            print("You are too young to be doing this")
            valid = True
        elif age >= 131:
            # If too old, user will be re-asked
            print("Please enter a valid age between(12 and 130)")
        else:
            # If valid age, code finishes
            print(age)
            valid = True
    except ValueError:
        # Prints error message if string is input
        print("Please enter a valid age(between 12 and 130)")
