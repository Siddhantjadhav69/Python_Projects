Height = int(input("Enter Your height : "))

if Height >= 120:
    print("congratulations You are Eligible for the Ride, So without wasting any time make a quick payment... fast  ")
    age = int(input("Enter your age : "))
    if age <=10:
        print("Your ticket price  will be 5$")
    elif age <=18:
        print("Your Tickit price will be 12$")
    else:
        print("Your ticket price will be 17$")
else:
    print("Sorry you are not eligible for the ride..")
print("Thank-you For the purchase")