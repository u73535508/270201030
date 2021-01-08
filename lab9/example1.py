def harmonicsum(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonicsum(n-1)
print(harmonicsum(5))