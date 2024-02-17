#The biggest and smallest number
num1=float(input("Enter num 1:"))
num2=float(input("Enter num 2:")) 
num3=float(input("Enter num 3:"))
if(num1>num2):
    if(num1>num3):
        biggest=num1
        if(num3>num2):
            smallest=num2
        else:
            smallest=num3
    else:
        biggest=num3
        smallest=num2
elif(num2>num3):
    biggest=num2
    if(num3>num1):
        smallest=num1
    else:
        smallest=num3
else:
    biggest=num3
    smallest=num1
print("Biggest=",biggest)
print("Smallest=",smallest)  