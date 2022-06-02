# import pandas as pd

# user_list_together = [['Julia Holman', 3, 'Pitachips'], ['Julia Holman', 4, 'Pitachips']]

# ticket_details = pd.DataFrame(user_list_together, columns=["Name", "Snack Amount", "Snack Type"])
# ticket_details.to_csv('ticket_details.csv', mode='a', index=True, header=False)
# print(ticket_details)
# print(len(ticket_details))

# import pandas as pd

# user_list_together = [['Julia Holman', 3, 'Pitachips', 5, "Popcorn"]]
# amount = ((len(user_list_together[0]) - 1) / 2)
# for i in range(len(user_list_together)):
    # if len(user_list_together[i]) == 3:
        # df = pd.DataFrame(user_list_together, columns=["Name", "Snack Amount", "Snack Type"])
        # print(df)
    # elif len(user_list_together[i]) == 5:
        #df = pd.DataFrame(user_list_together, columns=["Name", "Snack Amount", "Snack Type", "Snack 2 Amount",
                                                       #"Snack 2 Type"])
        #print(df)
# df.to_csv('existing.csv', mode='a', index=False, header=False)
# df = pd.read_csv('ticket_sales.csv')
# print(df.to_string())\import
import pandas as pd

user_list = [["Name", "ticket amount", "ticket price", 0, 0, 0, 0, 0, "snack price", "payment method", "total price"]]
singular_ticket = pd.DataFrame(user_list, columns=["Name", "Ticket Amount", "Total Ticket Price", "Popcorn", "M&M's",
                                                   "Pita Chips", "Orange Juice", "Water", "Snack Price",
                                                   "Payment method", "Order total"])
print(singular_ticket)
