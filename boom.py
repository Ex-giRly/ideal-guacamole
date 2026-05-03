from tkinter import *

window = Tk()
window.title("Event App")
window.geometry("200x150")

label = Label(window, text="Press a key or Click!")
label.pack()

def handle_key_press(event):
    label.config(text="Key: " + event.char)

def handle_click(event):
    label.config(text="Button Clicked! ")

window.bind("<Key>", handle_key_press)

button = Button(window, text="Click Me")
button.pack()
window.bind("<Button-1>", handle_click)

window.mainloop()

