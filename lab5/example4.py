def_password = "abc123"


while True:
  password = input("Enter a password:")
  
  if def_password == password:
    print ("welcome")
    break
  elif (password == "help") :
    print(def_password[0])
  else:
    print("Wrong")

    