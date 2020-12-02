
esitlik1 = input("Eşitlik giriniz:\n")
esitlik2 = input("Eşitlik giriniz:\n")
esitlik1sol = esitlik1.split("=")[0]
esitlik1sag = esitlik1.split("=")[1]
esitlik2sol = esitlik2.split("=")[0]
esitlik2sag = esitlik2.split("=")[1]

list1x = []
list1y = []
list1k = []
list1xx=[]
list1yy=[]
list1kk=[]
list1xxx=[]
list1yyy=[]
list1kkk=[]
list1xxxx=[]
list1yyyy=[]
list1kkkk=[]
sign =0
sign2 =0
sign3 =0
sign4 =0
for i in range(len(esitlik1sol)):
    if (esitlik1sol[i]) == "+" or (esitlik1sol[i] == "-"):
        if "x" not in esitlik1sol[sign:i] and "y" not in esitlik1sol[sign:i] and sign != 0:
            list1k.append(int(esitlik1sol[sign:i]))
        sign = i
    elif esitlik1sol[i] == "x":
        list1x.append(int(esitlik1sol[sign:i]))
    elif esitlik1sol[i] == "y":
        list1y.append(int(esitlik1sol[sign:i]))
    elif i == len(esitlik1sol)-1 and "x" not in esitlik1sol[sign:i] and "y" not in esitlik1sol[sign:i]:
        list1k.append(int(esitlik1sol[sign:i + 1]))



for i in range(len(esitlik1sag)):
    if (esitlik1sag[i]) == "+" or (esitlik1sag[i] == "-"):
        if "x" not in esitlik1sag[sign2:i] and "y" not in esitlik1sag[sign2:i] and sign2 != 0:
            list1kk.append(int(esitlik1sag[sign2:i]))
        sign2 = i
    elif esitlik1sag[i] == "x":
        list1xx.append(int(esitlik1sag[sign2:i]))
    elif esitlik1sag[i] == "y":
        list1yy.append(int(esitlik1sag[sign2:i]))
    elif i == len(esitlik1sag)-1 and "x" not in esitlik1sag[sign2:i] and "y" not in esitlik1sag[sign2:i]:
        list1kk.append(int(esitlik1sag[sign2:i + 1]))




for i in range(len(esitlik2sol)):
    if (esitlik2sol[i]) == "+" or (esitlik2sol[i] == "-"):
        if "x" not in esitlik2sol[sign3:i] and "y" not in esitlik2sol[sign3:i] and sign3 != 0:
            list1kkk.append(int(esitlik2sol[sign3:i]))
        sign3 = i
    elif esitlik2sol[i] == "x":
        list1xxx.append(int(esitlik2sol[sign3:i]))
    elif esitlik2sol[i] == "y":
        list1yyy.append(int(esitlik2sol[sign3:i]))
    elif i == len(esitlik2sol)-1 and "x" not in esitlik2sol[sign3:i] and "y" not in esitlik2sol[sign3:i]:
        list1kkk.append(int(esitlik2sol[sign3:i + 1]))



for i in range(len(esitlik2sag)):
    if (esitlik2sag[i]) == "+" or (esitlik2sag[i] == "-"):
        if "x" not in esitlik2sag[sign4:i] and "y" not in esitlik2sag[sign4:i] and sign4 != 0:
            list1kkkk.append(int(esitlik2sag[sign4:i]))
        sign4 = i
    elif esitlik2sag[i] == "x":
        list1xxxx.append(int(esitlik2sag[sign4:i]))
    elif esitlik2sag[i] == "y":
        list1yyyy.append(int(esitlik2sag[sign4:i]))
    elif i == len(esitlik2sag)-1 and "x" not in esitlik2sag[sign4:i] and "y" not in esitlik2sag[sign4:i]:
        list1kkkk.append(int(esitlik2sag[sign4:i + 1]))




soldakixkatsayısı1 = sum(list1x) + (-1*sum(list1xx))
soldakiykatsayısı1 = sum(list1y) + (-1*sum(list1yy))
sabit1 = (-1*sum(list1k)) + sum(list1kk)
soldakixkatsayısı2 = sum(list1xxx) + (-1*sum(list1xxxx))
soldakiykatsayısı2 = sum(list1yyy) + (-1*sum(list1yyyy))
sabit2 = (-1*sum(list1kkk)) + sum(list1kkkk)

if soldakixkatsayısı1>=0:
    soldakixkatsayısı1 = "+"+str(soldakixkatsayısı1)
if soldakiykatsayısı1>=0:
    soldakiykatsayısı1 = "+"+str(soldakiykatsayısı1)
if sabit1>=0:
    sabit1 = "+"+str(sabit1)
if soldakixkatsayısı2>=0:
    soldakixkatsayısı2 = "+"+str(soldakixkatsayısı2)
if soldakiykatsayısı2>=0:
    soldakiykatsayısı2 = "+"+ str(soldakiykatsayısı2)
if sabit2>=0:
    sabit2 = "+"+str(sabit2)

print("Simplfied form for two equetions")
print(str(soldakixkatsayısı1)+"x"+str(soldakiykatsayısı1)+"y"+"="+str(sabit1))
print(str(soldakixkatsayısı2)+"x"+str(soldakiykatsayısı2)+"y"+"="+str(sabit2))
