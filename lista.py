from tkinter import *

root = Tk()
listbox = Listbox(root)

items = (
            "Python",
            "C",
            "C++",
            "C#",
            "Java",
            "JavaScript",
            "Visual Basic"
        )

listbox.insert(0, *items)
 
listbox.pack()

lb1 = Label(text="Lenguajes de programación")
lb1.pack()
root.mainloop()