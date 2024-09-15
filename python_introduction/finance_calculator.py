# user input financial data
monthy_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
# calculate monthly savings
Monthly_savings = monthy_income - monthly_expenses
# project annual savings
Projected_savings = Monthly_savings * 12 + Monthly_savings * 0.05

# Outputs
print(f"Your monthly savings are: ${Monthly_savings:}")
print(
    f"Projected savings after one year, with interest, is: ${Projected_savings:}")
