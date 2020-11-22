gpa = float(input("Enter your GPA:"))
nol = float(input("Enter your number of lectures:"))
if gpa<2 :
  if nol<47 :
    print("Not enough number of lectures and GPA!")
  else:
    print("Not enough GPA!")
elif nol<47:
    print("Not enough number of lectures!")
else:
  print("GRADUATED!")