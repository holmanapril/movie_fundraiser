# Functions
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


def ticket_price():
    global age
    cost = 0
    # If age is less than 16 cost = 7.5
    if age < 16:
        cost += 7.5
    # If age is between 16 and 64 cost = 10.5
    elif 16 <= age <= 64:
        cost += 10.5
    # Anything else = 6.5
    else:
        cost += 6.5
    print("${:.2f}".format(cost))


# Main Routine
age = user_age("How old are you?", "Please enter a valid age between(12 and 130)",
               "You are too young to be doing this")
if age >= 12:
    ticket_price()
