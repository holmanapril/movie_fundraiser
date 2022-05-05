# Functions
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


def snacks(question, error, question_2, error_2, question_3):
    snack_choices = ["Popcorn", "M&M", "Pitachips", "Orangejuice", "Water"]
    keep_going = False
    while keep_going is False:
        snack_yes_no = str(input(question_3)).lower().strip()
        if snack_yes_no == "y" or snack_yes_no == "yes":
            valid = False
            print(question)
            while not valid:
                user_choice = str(input()).title().strip()
                if user_choice not in snack_choices:
                    print(error)
                else:
                    print(user_choice)
                    valid = False
                    while not valid:
                        try:
                            user_snack_amount = int(input(question_2))
                            if user_snack_amount <= 0:
                                print(error_2)
                            elif user_snack_amount >= 6:
                                print(error_2)
                            else:
                                print(user_snack_amount)
                                valid = True
                        except ValueError:
                            print(error_2)
        else:
            keep_going = True


def payment(question, error):
    valid = False
    print(question)
    while not valid:
        try:
            payment_method = int(input())
            if payment_method == 1:
                payment_method = "Cash"
                return payment_method
            elif payment_method == 2:
                payment_method = "Credit"
                return payment_method
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine
not_blank("What is your name?", "Please enter a valid full name(first and last name)")
user_age("How old are you?", "Please enter a valid age between(12 and 130)",
         "You are too young to be doing this")
age = user_age("How old are you?", "Please enter a valid age between(12 and 130)",
               "You are too young to be doing this")
if age >= 12:
    ticket_price()
snacks("What snack would you like?", "Please enter a valid snack choice(Please do not put spaces between words",
       "How many would you like?", "Please enter a valid amount(The maximum you can order of each snack is 5)",
       "Would you like to order any/more snacks?\nThe Options are:\nPopcorn\nM&M\nPita chips\nOrange Juice\nWater?")
payment("Will you be paying cash or credit?(enter 1 or 2)\nIf paying with credit "
        "there will be a surcharge of 2% to the final price\nOption 1                "
        "Option 2\nCash                    Credit", "Please enter a valid input(1 or 2)"
        "\nOption 1                "
        "Option 2\nCash                    Credit")
