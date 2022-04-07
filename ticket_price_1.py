age = 32
cost = 0
if age < 16:
    cost += 7.5
elif age > 15 or age < 65:
    cost += 10.5
else:
    cost += 6.5


print(cost)
