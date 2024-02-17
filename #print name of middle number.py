#print name of middle number
num1=float(input("Enter num 1:"))
num2=float(input("Enter num 2:"))
num3=float(input("Enter num 3:"))
if(num1>num2):
    if(num1>num3):
        if(num3>num2):
            print("Middle num=num3")
        else:
            print("Middle num=num2")
    else:
        print("Middle num=num1")
elif(num2>num3):
    if(num3>num1):
        print("Middle num=num3")
    else:
        print("Middle num=num1")
else:
    print("Middle num=num2")