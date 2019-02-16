### print("Enter your age: ", end='\n')

age = int(input("Enter your age = "))

if (age <= 0):
    print("Invalid value")
elif (age <=3):
    print("baby")
elif (age<=12):
    print("Old baby")
elif (age<=18):
    print("Teenager")
elif (age<=60):
    print("Old")
elif (age<=90):
    print("Very old")
else:
    print("Immortal")

