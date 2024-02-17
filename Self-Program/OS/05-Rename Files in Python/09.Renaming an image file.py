import os
import glob

folder = r"E:\Golrang\images\\"
for count, filename in enumerate(os.listdir(folder)):
    oldname = folder + filename
    newname = folder + "07-08-2023_" + str(count + 1) + ".jpg"
    os.rename(oldname, newname)

# printing the changed names
print(glob.glob(folder + "*.*"))
