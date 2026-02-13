# Write a programm to check a given "Year" is a Leapyear or not.

year = int(input(" Enter a year :- "))

if(year % 4 == 0 and year % 100 != 0  or year % 400 == 0 ):
    print(f" This Year {year} is a leap year")
else:
    print(f" This Year {year} is not a leap year")

#or

print("Leap year " if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "Not a Leao Year")


 