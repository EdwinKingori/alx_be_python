# user input financial data
monthy_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

# calculate monthly savings
monthly_savings = monthy_income-monthly_expenses
print(f"Your monthly savings are: ${monthly_savings}")

# interest rate
interest_rate = 0.05

# project annual savings
projected_savings = monthly_savings * 12 + \
    (monthly_savings * 12 * interest_rate)
print(
    f"Projected savings after one year, with interest, is: ${projected_savings}")
