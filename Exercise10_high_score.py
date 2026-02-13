# You are going to write a program that Cal. the heigth score frome a list of scores.
students_scores = []
n = int(input("Enter no._Students = "))
for i in range (0,n):
    a = (int(input("Enter a Scores = ")))
    students_scores.append(a)
    i += 1
heighest_score = 0
for score in students_scores:
    if score > heighest_score:
        heighest_score = score  
print(f"The Highest Score in the Class is : {heighest_score} ")