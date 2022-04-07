age = int(input("How old are you?"))
cost = 0
if age < 16:
    cost += 7.5
elif 16 <= age <= 64:
    cost += 10.5
else:
    cost += 6.5

print(age)
print(cost)
