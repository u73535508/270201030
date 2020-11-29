studentsScores = []
averages = []

amount_of_student = int(input("How many students are there? "))

for i in range(1,amount_of_student+1):
  print("Student",i)
  midterm1 = float(input("Enter your first midterm:"))
  midterm2 = float(input("Enter your second midterm:"))
  final = float(input("Enter your final score:"))

  studentsScores.append([midterm1,midterm2,final])

print(studentsScores)

for i in studentsScores:
    avg = 0
    avg = avg + i[0] * 0.3
    avg = avg + i[1] * 0.3
    avg = avg + i[2] * 0.4
    averages.append([avg])

print("Average of students points", averages)


