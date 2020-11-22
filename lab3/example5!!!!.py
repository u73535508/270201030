day = int(input("Enter a day:"))
month = input("Enter a month:")

spring = ["March","April","May","June"]
summer = ["June","July","August","September"]
fall= ["September","October","November","December"]
winter= ["December","January","February","March"]

if month in spring:
if month == "March" and day >= 20:
    print("Season is spring.")
else:
    print("Season is winter")
elif month == "June" and day < 21:
    print("Season is spring.")
  else:
    print("Season is summer.")
