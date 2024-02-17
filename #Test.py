#Test
with open('soli.txt','r') as file:
    #read first 3 line:
    for i in range(3):
        print(file.readline().strip())