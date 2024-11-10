print("Welcome to the love calculator !")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

Count = name1 + name2 

Lower = Count.lower()

t = Lower.count("t")
r = Lower.count("r")
u = Lower.count("u")
e = Lower.count("e")

true = t + r + u + e

l = Lower.count("t")
o = Lower.count("r")
v = Lower.count("u")
e = Lower.count("e")

love = l + o + v + e

score = int(str(true) + str(love))

if score <10 or score >90 :
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >39 and score <51:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your Score is {score}")
