with open("province.txt", "r") as f:
    informations = f.readlines()
    sözlük = {}
    cities = []
    possible1 = []
    possible2 = []
    kordinatlarx = []
    kordinatlary = []
    for information in informations:
        information = information.replace("\n", "")
        information = information.split(",")
        information[0] = information[0].upper()
        cities.append(information[0])
        cities.sort()
        kordinatlarx.append(information[1])
        kordinatlary.append(information[2])
        sözlük[information[0]] = information[1], information[2]
    while True:
        departure = input("Departure province:\n").upper()
        if departure in cities:
            break
        else:
            print("Province not found!")
            length = len(departure)
            öneri = ""
            for i in cities:
                if i[:length] == departure[:length]:
                    öneri = öneri + i
                    öneri = öneri + " "
        if öneri != "":
            print("Possible provinces:",öneri)
    while True:
        arrival = input("Arrival province:\n").upper()
        if arrival in cities:
            break
        else:
            print("Province not found!")
            length = len(arrival)
            öneri = ""
            for i in cities:
                if i[:length] == arrival[:length]:
                    öneri = öneri + i
                    öneri = öneri + " "
        if öneri != "":
            print("Possible provinces:", öneri)
    types = ["CAR", "BICYCLE", "MOTORCYCLE"]
    while True:
        travel_type = input("Enter travel type:\n").upper()
        if travel_type in types:
            break
    print("I am calculating the distance between", departure, "and", arrival, "...")
    a = sözlük[departure][0]
    a = float(a)
    b = sözlük[arrival][0]
    b = float(b)
    c = sözlük[departure][1]
    c = float(c)
    d = sözlük[arrival][1]
    d = float(d)
    distance = (((a-b)**2 + (c-d)**2)**0.5)*100
    distance = round(distance, 2)
    print("Distance:", distance)
    if travel_type == "CAR":
        time = distance/90
    elif travel_type == "BICYCLE":
        time = distance/25
    else:
        time = distance/80
    hours = int(time//1)
    minutes = (time-hours)*60
    minutes = int(minutes//1)
    print("Approximate time with", travel_type, ":", hours, "hours", minutes, "minutes")
