numbers= int(input("How many numbers:"))
count = 0
for i in range(1,numbers+1):
  x = int(input("Enter a number:"))
  if x % 2 == 0:
    count= 1 + count
print((count/numbers)*100) 