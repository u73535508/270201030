books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
books_dict ={}
for i in books:
    i =i.replace("'","")
    i =i.replace(" ","")
    letters=len(i)
    unique =len(set(i))
    books_dict[i]=letters,unique

print(books_dict)