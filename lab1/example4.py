gpa = int(input("Enter your GPA:"))
nol = int(input("Enter the number of lectures:"))
if gpa < 2.0 and nol < 47 :

  print("Not enough number of lectures and GPA!")

if gpa >= 2.0 and nol < 47 :

  print("Not enough number of lectures!")

if gpa < 2.0 and nol >= 47 :

  print("Not enogh GPA!")

else :

  print("Graduated!")