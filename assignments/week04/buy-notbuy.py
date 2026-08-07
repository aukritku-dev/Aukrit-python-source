prices = []

print("Enter prices of 6 items:")
for i in range(6):
    price = int(input(f"Item {i+1}: "))
    prices.append(price)

print()

budget = int(input("Enter total budget: "))
print()

total_spent = 0      
bought_items = []    

for i in range(6):
    if total_spent + prices[i] <= budget:
        total_spent += prices[i]
        bought_items.append(prices[i])
        print(f"Item {i+1} = {prices[i]} -> buy")
    else:
        print(f"Item {i+1} = {prices[i]} -> cannot buy")
    print(f"Current total = {total_spent}")
    print()

print(f"Bought items: {bought_items}")
print(f"Total spent: {total_spent}")
print(f"Remaining budget: {budget - total_spent}")