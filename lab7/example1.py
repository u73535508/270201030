names = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]

for i in names:
    if i[1] <18:
        names.remove(i)
#names = [("Jon",15),("Bran",10)]
for i in names:
    print(i[0])