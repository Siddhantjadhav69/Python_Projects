Height = int(input("Enter Your height : "))
bill = 0

if Height >= 120:
    print("congratulations You are Eligible for the Ride, So without wasting any time make a quick payment... fast  ")
    age = int(input("Enter your age : "))
    if age <=10:
        bill = 5
        print("Your ticket price  will be 5$")
    elif age <=18:
        bill = 12
        print("Your Tickit price will be 12$")
    elif age <=43:
        bill = 17
        print("Your ticket price will be 17$")
    elif age >=45 and age <=55:   
        print("Your Tickit is free ")
    else:
        print("your Bill will be 20$")      
    Photo = input("Do you want a photo? Y or N : ")
    if Photo == "Y":
        bill = bill + 3  
        print(f"Your Total will be ${bill}")

else:
    print("Sorry you are not eligible for the ride..")
print("Thank-you For the purchase")