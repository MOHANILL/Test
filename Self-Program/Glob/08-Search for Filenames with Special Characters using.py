import glob

print("All JPEG's files")
print(glob.glob("*.jpg"))

print("JPEGs files with special characters in their name")
# set of special characters _, $, #
char_seq = "_$#"
for char in char_seq:
    esc_set = "*" + glob.escape(char) + "*" + ".jpg"
    for file in (glob.glob(esc_set)):
        print(file)
