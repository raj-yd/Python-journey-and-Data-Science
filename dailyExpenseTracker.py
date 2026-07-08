expense=[int(i) for i in input("Enter Expence of 7 days separeted by space : ").split()]
print(f"Total Expanses - {sum(expense)}")
print(f"Highest Expanse - {max(expense)}")
print(f"Lowest Expanse - {min(expense)}")
print(f"Average Expanse - {sum(expense)/7}")

#method 2
# expense = []

# for i in range(7):
#     val = int(input(f"Enter expense for day {i+1}: "))
#     expense.append(val)
# print(f"Total Expense - {sum(expense)}")
# print(f"Highest Expense - {max(expense)}")
# print(f"Lowest Expense - {min(expense)}")
# print(f"Average Expense - {sum(expense)/len(expense)}")