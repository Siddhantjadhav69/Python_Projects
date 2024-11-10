print("Welcome to the Pizzas !")
size = input("What size do you want? S , M or L : ")
pepperoni = input("Do you want pepperoni?  Y or N : ")
cheese = input("Do you want extra cheese? Y or N : ")
Bill = 0
if size == "S":
   Bill += 15
elif size == "M":
   Bill += 20
elif size == "L":
   Bill += 25 

if pepperoni == "Y":
   if size == "S":
      Bill += 2
   else:
      Bill+=3
if cheese == "Y":
   Bill += 1
print(f"Your Total Bill will be : ${Bill}")