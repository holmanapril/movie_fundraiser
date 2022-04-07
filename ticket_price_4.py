def ticket_price(question, error):
    cost = 0
    age = 0
    # Asks user what their age is
    print(question)
    valid = False
    while not valid:
        try:
            age = int(input())
            # If age is less than 16 the code finishes
            if age < 16:
                cost += 7.5
                valid = True
            # if age between 16 and 64 cost = 10.5 and finishes
            elif 16 <= age <= 64:
                cost += 10.5
                valid = True
            else:
                cost += 6.5
                valid = True
        # If invalid input is entered error message is printed
        except ValueError:
            print(error)
    print(age)
    print(cost)


ticket_price("How old are you?", "Please enter a valid age")
