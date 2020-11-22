number1 = float(input("Enter a number:"))
number2 = float(input("Enter a number:"))
number3 = float(input("Enter a number:"))

if number1<number2:
  if number1<number3:
    print("The minimum of them is",number1)
  else:
    print("The minimum of them is",number3)
else:
  print("The minimum of them is",number2)