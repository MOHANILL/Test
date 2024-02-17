with open('read_demo.txt', 'r') as file:
    # read first 3 lines
    for i in range(6):
        print(file.readline().strip())
