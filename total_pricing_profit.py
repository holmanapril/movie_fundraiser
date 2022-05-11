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
    global cost
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
    print("Your ticket will cost ${:.2f}\n".format(cost))
    return cost


def snacks(question_1, question_2, question_3, error):
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
                    if user_choice >= 5 or user_choice < 0 or user_snack_amount > 5 or user_snack_amount < 1:
                        print(error)
                    else:
                        snack_price = snack_prices[user_choice - 1] * user_snack_amount
                        snack_price_total += snack_price
                        print("Your choice of {} {} costs: ${:.2f}\n".format(user_snack_amount, snack_choices[user_choice - 1], snack_price))
                        options = True
            elif yes_no == "n" or yes_no == "no":
                print("Total price of your snacks is:${}".format(snack_price_total))
                return snack_price_total
        except ValueError:
            print(error)


def payment(question, error):
    global payment_method
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


def profit():
    snack_price_total_profit = snack_price_total * 0.2
    ticket_profit = cost - 5
    total_price = snack_price_total + cost
    if payment_method == "Credit":
        surcharge = total_price * 0.02
        total_price += surcharge
    print("The total price is: ${}".format(total_price))
    total_profit = snack_price_total_profit + ticket_profit
    print("Profit: ${}".format(total_profit))


# Main Routine
global snack_price_total
global cost
global payment_method
age = user_age("How old are you?", "Please enter a valid age between(12 and 130)",
               "You are too young to be doing this")
if age >= 12:
    ticket_price()
    snacks("Do you want to order some/more snacks?\n", "Pick a snack(pick the number you want)\n\nThe options are:\n"
           "1. Popcorn: $2.50\n2. M&M: $3.00\n3. Pitachips: $4.50\n4. Orange Juice: $3.25\n5. Water: $2.00\n",
           "Choose an amount(maximum is 5)", "Please enter a valid snack number")
    payment("Will you be paying cash or credit?(enter 1 or 2)\nIf paying with credit "
            "there will be a surcharge of 2% to the final price\nOption 1                "
            "Option 2\nCash                    Credit", "Please enter a valid input(1 or 2)"
            "\nOption 1                "
            "Option 2\nCash                    Credit")
    profit()
