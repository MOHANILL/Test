f=open("C:\\test.txt","r")
data=f.read()

file_new=open("C:\\new_file.txt","w")
file_new.writelines(data)
file_new.close()
f.close()
       
