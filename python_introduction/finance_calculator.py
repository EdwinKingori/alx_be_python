# user input financial data
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
# calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
# project annual savings
Projected_savings = monthly_savings * 12 + monthly_savings * 0.05

# Outputs
print(f"Your monthly savings are: ${monthly_savings:}")
print(
    f"Projected savings after one year, with interest, is: ${Projected_savings:}")
