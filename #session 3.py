#session 3
ali=[3,4,"mohsen", True]
print(ali)
##
moli=["kratos","atreus", 44,True]
moli.insert(1,"odin")
print(moli)
moli[:3]=['ghule barare']
moli[2:]=[False]
print(moli)
print("ghule barare:\" takzib mikonam Hadi farahani\"")
##
list0=["Reza","seza"]
tuple0=("tereza",)
list0.extend(tuple0)
print(list0)
##
list1=["mohi", "soli", "koli"]
list1.append("roozi")
print(list1)
list1.remove("koli")
print(list1)
list1.pop()
print(list1)
del list1[1]
print(list1)
list1.clear()
print(list1)
##
i=0
list2=["mohammad", "roozi","soozi"]
while i<len(list2):
    print(list2[i])
    i+=1
for x in range(len(list2)):
    print(list2[x])
for s in (list2):
    print(s)
##
list2.sort()
print(list2)
list2.sort(reverse= True)
print(list2)
list3=[]
for i in list2:
    if "a" in i:
        list3.append(i)
print(list3)
##
list4=list0.copy()
print(list4)
list4.clear()
for x in (list0):
    if("R" in x or "r" in x):
       list4.append(x) 
       print(list4)
s