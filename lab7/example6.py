numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
intersections = []
numbers1=set(numbers1)
numbers2=set(numbers2)
for i in numbers1:
    if i in numbers2:
        intersections.append(i)
print("Intersection",intersections)
union = list(numbers2)+list(numbers1)
print("Union",set(union))