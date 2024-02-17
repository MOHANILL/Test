import glob

print("All JPEG's Files")
print(glob.glob("*.jpg"))

print("Jpeg with specail Chatercters")

especial="_$#"
for char in especial:
    especial_set="*"+glob.escape(char)+"*"+".jpg"
    for file in (glob.glob(especial_set)):
        print(file)
