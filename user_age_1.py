# Asks for users age
age = int(input("How old are you?"))
if age <= 11:
    # If user to young it prints saying so
    print("You are too young to be doing this")
elif age >= 131:
    # If over 131 it asks to enter a valid age
    print("Please enter a valid age between(12 and 130)")
else:
    # If a valid age is entered it reprints the age
    print(age)
