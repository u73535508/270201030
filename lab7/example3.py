books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
books_dict ={}
for i in books:
    i =i.replace("'","")
    i =i.replace(" ","")
    letters=len(i)
    unique =len(set(i))
    avg = (letters+unique)/2
    books_dict[i]=letters,unique,avg
for i in books_dict.items():
    print(i)