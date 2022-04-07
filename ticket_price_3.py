valid = False
while not valid:
    try:
        age = int(input("How old are you?"))
        cost = 0
        if age < 16:
            cost += 7.5
            valid = True
        elif 16 <= age <= 64:
            cost += 10.5
            valid = True
        else:
            cost += 6.5
            valid = True
    except ValueError:
        print("Please enter a valid age")


print(age)
print(cost)
