a=0
b=1
x = int(input("how long is gonna be continue?"))
for i in range(1,x+1):
  c = a+b
  a=b
  b=c
  print(a)