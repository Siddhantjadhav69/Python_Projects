Year = int(input("Enter the Year : "))

if Year % 4 ==0:
    if Year % 100 ==0:
        if Year % 400 ==0:
            print("Yes I'ts a leap year!")
        else: 
            print("No I'ts Not.")
    else:
        print("Yes I'ts a leap year")
else:
    print("No I'ts Not a leap Year")