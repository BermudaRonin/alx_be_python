# Prompt the user for their monthly income and expenses.

monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

# Calculate Monthly Savings

monthly_savings = float(monthly_income) - float(monthly_expenses)
print("Your monthly savings are $" + str(monthly_savings) + ".")

# Calculate the projected savings after one year.

interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $" + str(projected_savings) +".")
