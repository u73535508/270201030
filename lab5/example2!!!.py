numbers= int(input("How many numbers:"))

for i in range(1,numbers+1):
  x=int(input("Enter an integer:"))
  if x%2==0:
    print((x/numbers)*100)
