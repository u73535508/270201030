employees ={}
whole_salaries =[]
max_salary = []
for i in range(5):
    name = input("Name:")
    salary = input("Salary:")
    employees[name] = salary
for i in employees.values():
    whole_salaries.append(i)
for i in range(3):
    max_salary.append(max(whole_salaries))
    whole_salaries.remove(max(whole_salaries))
for a,b in employees.items():
    if b in max_salary:
        print(a)