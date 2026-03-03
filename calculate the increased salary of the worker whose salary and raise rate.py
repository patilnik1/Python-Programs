salary = int(input("Enter salary: "))
raise_percent = float(input("Salary raise rate (%): "))

new_salary = salary + (salary * raise_percent / 100)

print("Increased salary:", new_salary)