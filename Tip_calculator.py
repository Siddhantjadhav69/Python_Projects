#Tip calculator 
print("Welcome to the tip calculator!")
total_bill = float(input("What Was the total bill? : "))
Percentage =int(input("What percentage tip would you like to give? 10, 12 ,15? : "))
split = int(input("How many people to split the bill with? : " ))

Tip = Percentage/100 * total_bill + total_bill

People = Tip / split
Final = round(People,2)
print(f"So, your per-person bill will be : {Final}")
