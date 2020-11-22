#ax^2 + bx + c

a = float(input("Enter the represented as 'A'"))
b = float(input("Enter the represented as 'B'"))
c = float(input("Enter the represented as 'C'"))

delta = (b**2) - (4*a*c)
rr1 = ((-1*b) + (delta**0.5))/ 2*a
rr2 = ((-1*b) - (delta**0.5))/ 2*a

if delta > 0:

  print("There are two real roots.These are:",rr1,"and",rr2)
elif delta < 0:
  print("There are two complex roots.These are:",rr1,"and",rr2)
else:
  print("There is one real root.This is",rr1)