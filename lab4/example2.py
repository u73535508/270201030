year = int(input("Enter a year:"))

if year % 4 == 0:
  if year % 400 != 0:
    print("Not leap year!")
  else:
    print("Leap year!")
else:
  print("Not leap year!")