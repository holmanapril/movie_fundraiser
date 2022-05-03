valid = False
print("Will you be paying cash or credit?(enter 1 or 2)\nIf paying with credit "
      "there will be a surcharge of 2% to the final price\nOption 1                "
      "Option 2\nCash                    Credit")
while not valid:
    try:
        payment_method = int(input())
        if payment_method == 1:
            print("Cash")
        elif payment_method == 2:
            print("Credit")
        else:
            print("Please enter a valid input(1 or 2)\nOption 1                "
                  "Option 2\nCash                    Credit")
    except ValueError:
        print("Please enter a valid input(1 or 2)\nOption 1                "
              "Option 2\nCash                    Credit")
