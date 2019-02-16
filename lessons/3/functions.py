def printNumber(number = 10):
    print ("This is VOID function and \n This is your number:: "+str(number) +'\n\n')

# printNumber(5)
# printNumber()

def clocks(hours, minutes, schemaKey = True):
    if(schemaKey):
        print(str(hours) + " : "+str(minutes))
    else:
        if (hours > 12):
            postfix = ' PM'
        else:
            postfix = ' AM'

        print(str(hours - 12) + " :  "+str(minutes) + postfix)

clocks(15, 26)
clocks(15, 26, True)
clocks(15, 26, False)

print ('asdsadasd', end='\n')
print ('asdsadasd')