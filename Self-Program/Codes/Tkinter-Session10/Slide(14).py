from tkinter import *
window = Tk()

window.title("Create Label")
window.geometry("300x300+500+250")

color1 = "blue"
color2 = "red"
color3 = "black" 
radiovar = IntVar()
def change_color():
    color = radiovar.get()
    if color == 1:
        window.configure(background = color1)
    elif color == 2:
        window.configure(background = color2)
    elif color == 3:
        window.configure(background = color3)

radio1 = Radiobutton(window, text= "Blue", relief = RIDGE, value = 1, variable = radiovar, command = change_color).grid(column = 0, row = 0)
radio2 = Radiobutton(window, text= "Red", relief = RIDGE, value = 2, variable = radiovar, command = change_color).grid(column = 0, row = 1)
radio3 = Radiobutton(window, text= "Blck", relief = RIDGE, value = 3, variable = radiovar, command = change_color).grid(column = 0, row = 2)


window.mainloop()