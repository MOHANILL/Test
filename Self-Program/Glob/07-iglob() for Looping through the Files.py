import glob

# using iglob
for item in glob.iglob("*.txt"):
    print(item)

# check type
print('glob()')
print(type(glob.glob("*.txt")))

print('iglob()')
print(type(glob.iglob("*.txt")))
