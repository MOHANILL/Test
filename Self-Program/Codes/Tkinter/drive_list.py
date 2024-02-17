import os 

def find_drive():

    drives = []

    for drive_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if os.path.exists(f'{drive_letter}:'):
            drives.append(f'{drive_letter}:')
        else:
            pass
    print(drives)

find_drive()