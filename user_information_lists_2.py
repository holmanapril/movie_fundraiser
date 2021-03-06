user_list_together = [['April Holman', 3, 'Pitachips']]
user_list = []


# Functions
def not_blank(question, error):
    global user_list
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
                user_list.append(user_name)
                return user_name
            else:
                # If spaces = equal 0, it prints error and then asks for input again
                print(error)


def snacks(question_1, question_2, question_3, error):
    global user_list
    global snack_price_total
    snack_price_total = 0
    snack_choices = ["Popcorn", "M&M", "Pitachips", "Orangejuice", "Water"]
    snack_prices = [2.50, 3.00, 4.50, 3.25, 2.00]
    valid = False
    while not valid:
        options = False
        try:
            yes_no = str(input(question_1)).strip().lower()
            if yes_no == "y" or yes_no == "yes":
                while not options:
                    user_choice = int(input(question_2))
                    user_snack_amount = int(input(question_3))
                    if user_choice >= 6 or user_choice < 0 or user_snack_amount > 5 or user_snack_amount < 1:
                        print(error)
                    else:
                        user_list.append(user_snack_amount)
                        user_list.append(snack_choices[user_choice - 1])
                        snack_price = snack_prices[user_choice - 1] * user_snack_amount
                        snack_price_total += snack_price
                        print("Your choice of {} {} costs: ${:.2f}\n".format(user_snack_amount,
                              snack_choices[user_choice - 1], snack_price))
                        options = True
            elif yes_no == "n" or yes_no == "no":
                print("Total price of your snacks is:${}".format(snack_price_total))
                return snack_price_total
        except ValueError:
            print(error)


# Main Routine
global snack_price_total
global cost
global payment_method
not_blank("What is your name?", "Please enter a valid full name(first and last name)")
snacks("Do you want to order some/more snacks?\n", "Pick a snack(pick the number you want)\n\nThe options are:\n"
       "1. Popcorn: $2.50\n2. M&M: $3.00\n3. Pitachips: $4.50\n4. Orange Juice: $3.25\n5. Water: $2.00\n",
       "Choose an amount(maximum is 5)", "Please enter a valid snack number")
user_list_together.append(user_list)
print(user_list)
print(user_list_together)

