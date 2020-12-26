def is_prime():
    a = int(input("Enter an integer:"))
    b = int(input("Enter an integer:"))
    for dividing in range(a+1,b):
        prime = True
        for divisor in range(2,a):
            if dividing%divisor==0:
                prime = False
        if prime :
            print(dividing)
is_prime()