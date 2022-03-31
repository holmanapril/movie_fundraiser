valid = False
while not valid:
    try:
        age = int(input("How old are you?"))
        if age <= 11:
            print("You are too young to be doing this")
            valid = True
        elif age >= 131:
            print("Please enter a valid age between(12 and 130)")
        else:
            print(age)
            valid = True
    except ValueError:
        print("Please enter a valid age(between 12 and 130)")
