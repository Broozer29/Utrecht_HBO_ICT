from tkinter import *
root = Tk()
root.geometry('400x400')
label = Label(master=root, text='Hello World', height=2)
label.pack()

button = Button(master=root, text='Druk hier')
button.pack(side = LEFT, fill = Y, pady=10)

root.mainloop()