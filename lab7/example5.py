password = input("Enter a password:") 
numbers="0123456789"
for i in password:
    if i in numbers:
        if len(password) >=8 and password.upper()!=password and password.lower()!=password:
            print("Valid")
        else:
            print("Not Valid")
            break