def user_age(question, error, error_2):
    global age
    valid = False
    print(question)
    # Continues to ask for input until valid input it entered
    while not valid:
        try:
            # Asks for age
            age = int(input())
            if age <= 11:
                # If too young, code will finish
                print(error_2)
                return age
            elif age >= 131:
                # If too old, user will be re-asked
                print(error)
            else:
                # If valid age, code finishes
                return age
        except ValueError:
            # Prints error message if string is input
            print(error)
