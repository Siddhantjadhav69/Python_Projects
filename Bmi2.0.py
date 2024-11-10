weight = float(input("Enter Your weight : "))
height = float(input("Enter your height : "))

Bmi = round(weight / height **2 )

if Bmi>18.5 :
    print(f"Sorry but Under {Bmi} You are Underweight.")
elif Bmi>25 :
    print(f"Under {Bmi} You are Normal-weight")
elif Bmi>30:
    print(f"Sorry but Above {Bmi} You are Overweight.")
elif Bmi>35 :
    print(f"Above {Bmi} You are Obese.")
else:
    print("Fuck off FatASS")