# user input financial data
monthy_income = int(input("Enter monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# calculate monthly savings
monthly_savings = monthy_income-monthly_expenses
print(f"Your monthly savings are: ${monthly_savings}")

# project annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(
    f"Projected savings after one year, with interest, is: ${projected_savings}")
