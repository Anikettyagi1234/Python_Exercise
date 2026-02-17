n = int(input("Entera no. = "))
sum = 0
for i in range (2,n+1):
    if i%2 == 0:
        print(i)
        sum = sum + i

print(f"Total sum of Even no . is  = {sum}")        


#or

n = int(input())
sum = 0
for i in range (2, n+1, 2):
    print(i)
    sum = sum + i
print(sum)