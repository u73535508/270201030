def get_evens(list):
    if len(list) == 0:
        return 0
    elif list[0] % 2==1:
        return 1 + get_evens(list[1:])
    elif list[0] % 2 == 0:
        return 0 + get_evens(list[1:])
print(get_evens([1,2,3,4]))