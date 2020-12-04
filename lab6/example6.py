
nestedArr = []
n = int(input('len of arr : '))
for i in range(n):
    c = []
    for j in range(n):
        c.append(int(input()))
    nestedArr.append(c)
tracesum = 0
for i in range(len(nestedArr)):
    tracesum += nestedArr[i][i]
print(tracesum)