#mini project 1
# Rent Calculator Program

rent = int(input("Enter house rent: ₹ "))
food_cost = int(input("Enter total food cost: ₹ "))
water_bill = int(input("Enter water bill amount: ₹ "))

cost_per_unit = int(input("Enter electricity cost per unit: ₹ "))
total_units = int(input("Enter total electricity units consumed: "))

members = int(input("Enter number of people: "))

# Calculate electricity bill
electricity_bill = cost_per_unit * total_units

# Calculate total expenses
total_expense = rent + food_cost + water_bill + electricity_bill

# Calculate per person share
per_person_amount = total_expense / members

print("\n------ Expense Summary ------")
print(f"Total Expense: ₹ {total_expense}")
print(f"Each person should pay: ₹ {per_person_amount:.2f}")

