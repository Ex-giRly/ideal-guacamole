from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry("250x200")
root.title("Virus scanner game")

def msg():
   result = random.choice(["Safe", "Suspicious","Virus found" ])
   messagebox.showinfo("Scan Result", result)
   
button = Button(root, text="Scan ", command=msg)
button.pack(pady=50)

root.mainloop()