n = int(input("How much enter a Heigths =  "))
students_heigths =[]
for i in range (0 ,n):
   a = (int(input("Enter a HEIGTH = "))  )  
   students_heigths.append(a)
   i += 1
total_heigth = 0
for heigth in students_heigths:
    total_heigth += heigth
print(f"Total_Heigth = {total_heigth} ")

total_students = 0
for students in students_heigths:
    total_students += 1
print(f"Total_students = {total_students}")

average_heigth = round(total_heigth / total_students)
print(f"average_heigth =  {average_heigth}")
