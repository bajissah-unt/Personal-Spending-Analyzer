transactions = [
    {"merchant" : "walmart", "category": "groceries", "amount": 120},
    {"merchant" : "Lavanderia", "category": "food", "amount": 10.32},
    {"merchant" : "shell", "category": "gas", "amount": 160},
    {"merchant" : "TotalWireless", "category": "phoneplan", "amount": 160}

]
#count the total amount
count = 0
for trans in transactions:
    count = count + trans["amount"]
print (f"The total transactions so far : ${count:.2f}")
highest_amount = 0

#calculate max and category
for trans in transactions:
    if trans["amount"]>highest_amount:
        highest_amount = trans["amount"]
        highest_merchant = trans["merchant"]

print (f"The highest money spent was ${highest_amount:.2f} at {highest_merchant}")

#calculate average
print (f"The average expenditure is {count/len(transactions):.2f}")

