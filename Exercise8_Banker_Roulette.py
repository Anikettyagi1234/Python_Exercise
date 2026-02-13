# you are going to write a programm that will select a "random_name" from a list of "name". 
# The person Selected will have to pay for everybodys "Food_Bill".

name1 = []
no_of_names = int(input("Enter a number of Members to be added = "))
for i in range (0,no_of_names):
    name = (input("Enter name  = "))
    name1.append(name)
    i += 1 
import random
num_item = len(name1)
random_choice = random.randint(0,num_item - 1)
print(f"{name1[random_choice]} is going to buy the meal today!")

