age = int(input("Enter your age: "))
ticket = int(3)
if age <6 or age>60:
  print("Ticket is free for you!")
elif age>=6 and age<=18:
  print("Ticket price is",ticket*0.5,"Tl for you!")
else:
  print("Ticket price is",ticket,"Tl for you! ")