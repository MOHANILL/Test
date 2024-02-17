"""
Renaming files with a Pattern
Sometimes we wanted to rename only those files that match a specific pattern. For example,
 renaming only pdf files or renaming files containing a particular year in their name.

The pattern matching is done using the glob module. The glob module is used to find the files and folders whose names follow a specific pattern.

We can rename files that match a pattern using the following steps: –

Write a pattern using wildcard characters
Use a glob() method to find the list of files that matches a pattern.
Iterate through the files in the folder
Change the name according to the new naming convention.
Note:Using the glob module we can search for exact file names or even specify part of it using the patterns created using wildcard characters.
"""
import glob
import os
valu_pattern=input("Enter Your Pattern :")
path=r"E:\ParentFolder\SubFolder\\"
# search text files starting with the word "sales"
pattern=path+valu_pattern + "*.pdf"

# List of the files that match the pattern
result=glob.glob(pattern)

count=1
for file_name in result:
    old_name=file_name
    new_name=path+'newfile_'+str(count)+".pdf"
    os.rename(old_name,new_name)
    count=count+1
#printing all revenue txt files
res=glob.glob(path+"newfile"+"*.pdf")
for name in res:
    print(name)
