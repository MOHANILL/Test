#session 6
def my_Func():
    print ("Hello world")
#my_Func()
print(my_Func())
##

import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))#day now
print(x.strftime("%B"))#month now
##
x1=datetime.datetime(2020,2,3)
print(x1)
##
from datetime import time
x2=time(11,25,20)
print("Hour:", x2.hour)
print("Minut:", x2.minute)
print("Second:", x2.second )
##
#fp=open('roozi.txt', 'x')
#fp.close()
##
fp=open('roozi.txt', 'w')
fp.write('Farbode mj key mimiri')
fp.close()
##
import os
print(os.listdir())
print(os.path.isfile('roozi.txt'))
##
with open(r'F:reza.txt', 'w') as reza:
    reza.write('maghroure jazab')
    pass
##
#path= r'G:Movie & series\amu\\'
#file_name='ahmad.txt'
#with open(os.path.join(path, file_name),'w')as fpp:
#    fpp.write('Reza jan')
##
file__path=r'F:python learn\BP\Test\neversnich.txt'
if os.path.exists(file__path):
    print('file already exists')
else:
    with open(file__path, 'w') as ffp:
        ffp.write('alhamdollah')