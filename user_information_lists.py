orders = []
tickets = 2
while tickets > 0:
    name = str(input("What is your name?"))
    age = int(input("How old are you?"))
    number = int(input("What is you favourite number"))
    food = str(input("What is your favourite food"))
    orders.append([name, age, number, food])
    print(orders)
    tickets -= 1

print(orders)
