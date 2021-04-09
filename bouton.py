from tkinter import *
root = Tk()
def myClick():
    myLabel=Label(root, text="vous avez obtenu:")
    myLabel.pack()
myButton = Button(root, text="piocher!", command=myClick )
myButton.pack()

root.mainloop()
