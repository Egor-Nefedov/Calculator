import tkinter
from tkinter import *
from tkinter import ttk


window = Tk()
window.title("Calculator")
window.geometry("500x600")
window.resizable(False, False)

pixel = PhotoImage(width=1, height=1)
buttons_text=["1","2","3","=","4","5","6","+","7","8","9","-","DEL","0","*","/"]
x=0
y=3
text="0"

def click_button(but):
    global text
    if but == "=":
        text = str(eval(text))
        label.config(text=text)
    elif but == "DEL":
        text="0"
        label.config(text=text)
    else:
        if text == "0":
            text = but
            label.config(text=text)
        else:
            text = text + but
            label.config(text=text)

label = Label(background="black", text=text, font="Times 30",fg="white")
label.grid(row=0, columnspan=4, sticky="we")

for button in buttons_text:
    click = lambda x=button: click_button(x)
    but = Button(window, image=pixel, text=button, width=100, height=100, compound="c", command=click)
    but.grid(column=x, row=y)
    x += 1
    if x > 3:
        x = 0
        y += 1
    but.place()

window.mainloop()