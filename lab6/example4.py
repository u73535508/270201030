
users_list2 = input("Enter numbers:(Seperate numbers with ',')")
users_list2 = users_list2.split(',')
result = []
for i in users_list2:
  if i not in result:
    result.append(i)
print(result)