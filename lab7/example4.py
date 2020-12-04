employees ={}
salaryy =[]
mak = []
for i in range(5):
    name = input("Name:")
    salary = input("Salary:")
    employees[name] = salary
for i in employees.values():
    salaryy.append(i)
for i in range(3):
    mak.append(max(salaryy))
    salaryy.remove(max(salaryy))
for a,b in employees.items():
    if b in mak:
        print(a)