monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")

monthly_savings = float(monthly_income) - float(monthly_expenses)
print(f"Your monthly savings are: {monthly_savings}")
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05)
print(f"Projected savings after one year, with interest, is: {projected_savings}")