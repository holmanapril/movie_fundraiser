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


payment("Will you be paying cash or credit?(enter 1 or 2)\nIf paying with credit "
        "there will be a surcharge of 2% to the final price\nOption 1                "
        "Option 2\nCash                    Credit", "Please enter a valid input(1 or 2)"
        "\nOption 1                "
        "Option 2\nCash                    Credit")
