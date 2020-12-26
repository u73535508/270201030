def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def print_primes_between(n,m):
    for x in range(n,m+1):
        if is_prime(x):
            print(x)
num1=int(input("Enter a smaller integer"))
num2=int(input("Enter a greater integer"))
print_primes_between(num1,num2)