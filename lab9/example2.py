def get_reversed(list):
    if len(list) == 0:
        return []
    else:
        return [list[-1]] + get_reversed(list[:-1])
print(get_reversed([1,2,3,4]))