from tkinter import *

def sel():
   selection = "As elegido la opción " + str(var.get())
   label.config(text = selection)
   
def reset():
    var.set(None)
    label.config(text = "")

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Opción 1", variable=var, value=1, command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Opción 2", variable=var, value=2, command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Opcion 3", variable=var, value=3, command=sel)
R3.pack( anchor = W)

B1 = Button(root, text="reset", command=reset)
B1.pack()

label = Label(root)
label.pack()

root.mainloop()