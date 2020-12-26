def level_of_password(password):
    if " " in password or len(password) < 8:
        return "Level 0"
    elif password.isalpha() or password.isnumeric():
        return "Level 1"
    elif password.isalnum():
        return "Level 2"
    else:
        return "Level 3"

password = input("Enter a password:\n")
print("Security level:","(",level_of_password(password),")")