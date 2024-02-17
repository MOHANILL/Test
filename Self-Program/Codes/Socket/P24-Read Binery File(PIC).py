f=open("a.png","rb")
data=f.read()

f1=open("new-a.png","wb")
f1.write(data)

f.close()
f1.close
