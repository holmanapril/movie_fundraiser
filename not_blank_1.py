valid = False
# Keeps running while loop until they enter a name that is not a digit
while not valid:
    # Asks what users name is
    name = str(input("What is your name?")).title()
    if name.isdigit():
        # Prints error message
        print("Please enter a valid name")
    else:
        valid = True
        # Prints name entered
        print(name)
