from tkinter import *

root = Tk()


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == '=':
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == 'c':
        scvalue.set('')
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root.geometry("900x600")
root.title('calculator')
scvalue = StringVar()
scvalue.set('')
screen = Entry(root, textvar=scvalue, font="lucida,40,bold")
screen.pack(fill=X, pady=10, padx=10)
f = Frame(root, bg='grey')
b = Button(f, text='9', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text='8', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text='7 ', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()
f = Frame(root, bg='grey')
b = Button(f, text='6', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text='5', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text='4', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()
f = Frame(root, bg='grey')
b = Button(f, text='3', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text='2', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text='1', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg='grey')
b = Button(f, text='0', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text='-', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text='*', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg='grey')
b = Button(f, text='/', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text='+', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text='=', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg='grey')
b = Button(f, text='c', padx=28, pady=29, font="lucida,40,bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()