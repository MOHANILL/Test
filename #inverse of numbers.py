#inverse of numbers
num=input("Enter a number:")
num1=int(num)
reverse=''
for i in range(len(num)):
    remain=num1%10
    num1//=10
    reverse+=str(remain)
print(int(reverse))