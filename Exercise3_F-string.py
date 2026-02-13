#  Creat a programm using math and f-string that tells us how many "Weeks" we have  left , if we live until 90 years old.
#  input yoour age and output a mssage with our time left in this formate :-
#  "You have x weeks left."

age = int(input("Enter your  current age :- "))
years = 90 - int(age)
weeks =  years * 52
days = weeks * 7
print(f" you have {weeks} weeks left and {days} Days left.")