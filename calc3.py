'''ARKAPRATIM GHOSH TECHNO MAIN SALTLAKE
OCTOBER 2021'''

from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "  =   ":
        if scvalue.get().replace(" ","").isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get().replace(" ",""))
            except Exception as e:
                value = "ERROR"

        scvalue.set(value)
        screen.update()
    elif text == "DEL":
        scvalue.set("")
        screen.update()
    elif text == " AC":
        quit()
    else:
        v=scvalue.get().replace(" ","")
        scvalue.set(v + text.replace(" ",""))
        screen.update()


root = Tk()
root.geometry("200x220")
root.minsize(200,220)

root.maxsize(200,220)
root.title("Calculator Arkapratim Ghosh ")
root.wm_iconbitmap("2")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="comicsansms 20 bold")
screen.pack(fill=X, ipadx=20, pady=10, padx=10)

f1=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)


b1=Button(f1,bg="grey",fg="black",text="  7  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="  8  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="  9  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="DEL",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text=" AC",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)


b1=Button(f1,bg="grey",fg="black",text="  4  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="  5  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="  6  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="   *  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="  /  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)


b1=Button(f1,bg="grey",fg="black",text="  1  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="  2  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="  3  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="   +  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="  -  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)


b1=Button(f1,bg="grey",fg="black",text="  0  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="  .  ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text=" **",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="   %   ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="grey",fg="black",text="  =   ",font="comicsans 10 bold")
b1.pack(side=LEFT,padx=1)
b1.bind("<Button-1>",click)
f1.pack()


root.mainloop()