'''
 write a programm that works out whether if a given number is an odd or even number.

Even number csn be divided by 2 with no reminder.

e.g 86 is even because 86 / 2 = 43

 '''

number = int(input(" Enter a number :- "))

if number % 2 == 0 :
    print(" Given number is \"EVEN\" ")

else:
    print(" Given number is \"ODD\"")
