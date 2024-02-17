#Detect equilateral triangle from its angles
ang1=float(input("Enter length of angle 1:"))
ang2=float(input("Enter length of angle 2:"))
ang3=float(input("Enter length of angle 3:"))
if(ang1>=0 and ang2>=0 and ang3>=0):                           #check that length of angles be positive
    if(ang1+ang2>ang3 and ang1+ang3>ang2 and ang2+ang3>ang1):  #check that number might make triangle
        if(ang1==ang2==ang3):
           print("<it is Equilateral triangle>")
        else:
           print("<it is NOT Equilateral triangle>")
    else:
         print("Your numbers can't make triangle!!!!")
else:
    print("Error:Angles' length can't be minus, try again!!!!")