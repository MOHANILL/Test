S = input("Enter a sentence:")
vowels = 'aeiou'
x=''
for letter in S:
    if letter in vowels:
        letter=letter.upper()
    x+=letter
print(x)
        
