day = int(input("Enter a day:"))
month = input("Enter a month:")

spring = ["March","April","May","June"]
summer = ["June","July","August","September"]
fall= ["September","October","November","December"]
winter= ["December","January","February","March"]

if month in spring:
  if month == "March" and day >= 20:
    print("Season is spring.")
  elif month == "March" and day < 20:
    print("Season is winter.")
  elif month == "June" and day <21:
    print("Season is spring")
  elif month == "June" and day >=21:
    print("Season is summer")
  else:
    print("Season is spring.")
  if month in summer:
    if month =="September" and day<22:
      print("Season is summer.")
    elif month == "September" and day>=22:
      print("Season is fall.")
    else:
      print("Season is Summer.")
    if month in fall:
      if month == "December" and day<21:
        print("Season is fall")
      elif month == "December" and day >=21:
        print("Season is winter.")
      else:
        print("Season is fall.")
        if month in winter:
          print("Season is winter.")