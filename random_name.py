import random
name = input("Give me the names, seperated by a comma ',' ")
names=name.split(", ")

length_of= len(names)

randomnames = random.randint(0,length_of -1)

will_pay = names[randomnames]

print("The prson who will pay is ",will_pay)