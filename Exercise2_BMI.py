# To find out a BMI. 

# BMI =weigth(kg)/ higth**2(m).

weigth_of_Body = float(input("Enter your Body weigth in (kg) :- " ))
heigth_of_Body = float(input("Enter your Heigth in (meter) :- ")) 
new_weigth_of_Body = int(weigth_of_Body)
new_heigth_of_Body = int(heigth_of_Body)
BMI =  (weigth_of_Body)/(heigth_of_Body)**2

print("BMI IS :- ", BMI)

if(BMI <= 18.5):
    print("You are in a under_Weigth ")
elif(18.5 < BMI < 24.9):
    print("You are in a Normal_Weigth ")
elif(25 < BMI < 29.9):
    print("You are in a Over_Weigth ")
elif(BMI > 30):
    print("You are in a obese ")
