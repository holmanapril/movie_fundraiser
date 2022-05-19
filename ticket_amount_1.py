def ticket_price_amount(question, error, error_2):
    cost = 0
    valid = False
    t_amount = 0
    while not valid:
        try:
            t_amount = int(input(question))
            for i in range(t_amount):
                age = int(input("What age will ticket {} be for?".format(i + 1)))
                try:
                    # Asks for age
                    if age <= 11:
                        # If too young, code will finish
                        print(error)
                        return age
                    elif age >= 131:
                        # If too old, user will be re-asked
                        print(error)
                        return age
                    else:
                        if age < 16:
                            print("Ticket {} will cost $7.50\n".format(i + 1))
                            cost += 7.5
                        elif 16 <= age <= 64:
                            print("Ticket {} will cost $10.50\n".format(i + 1))
                            cost += 10.5
                        else:
                            print("Ticket {} will cost $6.50\n".format(i + 1))
                            cost += 6.5
                except ValueError:
                    # Prints error message if string is input
                    print(error_2)
                valid = True
        except ValueError:
            print(error_2)
        if valid:
            print("Total cost of {} tickets is ${:.2f}".format(t_amount, cost))


ticket_price_amount("How many tickets do you want", "That is not a valid age(Please rerun the programme)",
                    "Please enter valid input")
