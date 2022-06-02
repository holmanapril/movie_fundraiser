import csv

orders = []
lines = 0

# read ticket sales from CSV
with open("ticket_details.csv") as csv_file:
    # CSV columns are
    # Name,Pitachips,PopCorn,OJ,Water,MandM
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        lines += 1
        orders.append(row)

# print the orders we loaded
print(" number of orders - {}".format(lines))

print(orders)

total_number_of_pita = 0
for order in orders:
    print("name : " + order[0])
    total_number_of_pita += int(order[1])
    # print("Pita qty : " + order[1])

print("total Pita ordered {} ".format(total_number_of_pita))
# add an order
orders.append(["Charlie Brown","1","2","3","4","5"])


# save order
with open("ticket_details.csv", "w") as updated_file:
    file_writer = csv.writer(updated_file, dialect='excel')
    for order in orders:
        file_writer.writerow(order)

updated_file.close()



