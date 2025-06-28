item1 = float(input("Enter the cost of item 1: "))  # ãËá 35
item2 = float(input("Enter the cost of item 2: "))  # ãËá 50
item3 = float(input("Enter the cost of item 3: "))  # ãËá 20
budget = float(input("Enter your budget: "))        # ãËá 150

total_cost = item1 + item2 + item3
print("Total cost =", total_cost)

if budget >= total_cost:
    difference = budget - total_cost
    print("You are within budget. Remaining amount:", difference)
else:
    difference = total_cost - budget
    print("You are over budget by:", difference)