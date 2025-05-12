# Salary with Bonus

name = input()
fixed_salary = float(input())
total_sales = float(input())

total_salary = fixed_salary + (total_sales * 0.15)
print(f"TOTAL = R$ {total_salary:.2f}")