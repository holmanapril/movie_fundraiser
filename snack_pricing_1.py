def snacks(question_1, question_2, question_3):
    snack_price_total = 0
    options = False
    snack_choices = ["Popcorn", "M&M", "Pitachips", "Orangejuice", "Water"]
    snack_prices = [2.50, 3.00, 4.50, 3.25, 2.00]
    valid = False
    while not valid:
        try:
            yes_no = input(question_1)
            if yes_no == "y" or yes_no == "yes":
                while not options:
                    user_choice = int(input(question_2))
                    user_snack_amount = int(input(question_3))
                    if user_choice >= 5 or user_choice < 0 or user_snack_amount > 5 or user_snack_amount < 1:
                        print("Please enter a valid number")
                    else:
                        options = True
                        snack_price_total += snack_prices[user_choice - 1] * user_snack_amount
                        print("${:.2f}".format(snack_price_total))
                        print("And your choices were {} {}".format(user_snack_amount, snack_choices[user_choice - 1]))
            elif yes_no == "n" or yes_no == "no":
                print("Total price of your snacks is:${}".format(snack_price_total))
                return snack_price_total
        except ValueError:
            print('Please enter a valid snack')


snacks("Do you want to order some/more snacks?", "Pick a snack(pick the number you want)\nThe options are:\n"
       "1. Popcorn: $2.50\n2. M&M: $3.00\n"
       "3. Pitachips: $4.50\n4.Orange Juice: $3.25\n5. Water: $2.00", "Choose an amount(maximum is 5)")
