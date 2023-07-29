from tkinter import *

root = Tk()
root.title("Simple Calculator")

root.configure(background = "black")



# establish the grid layout

e = Entry(root, width = 32, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 2 , pady = 5)
e.configure(background = "black", foreground = "white")


# define the button functions

def myclick(n):
    temp = e.get()
    e.delete(0, END)
    e.insert(0, str(temp)+str(n))


def clear():
    temp = e.get()
    e.delete(0, END)
    e.insert(0, str(temp)[:-1])


def allclear():
    e.delete(0, END)

def equal():
    snum = int(e.get())
    e.delete(0, END)
    if meth == 'a':
        e.insert(0, fnum + snum)
    elif meth == 's':
        e.insert(0, fnum - snum)
    elif meth == 'm':
        e.insert(0, fnum * snum)
    elif meth == 'd':
        if snum == 0:
            e.insert(0, "                    Odra angutu")
        else:
            e.insert(0, fnum / snum)

def add():
    global fnum, meth
    fnum = int(e.get())
    meth = 'a'
    allclear()

def sub():
    global fnum, meth
    fnum = int(e.get())
    meth = 's'
    allclear()

def mul():
    global fnum, meth
    fnum = int(e.get())
    meth = 'm'
    allclear()

def div():
    global fnum, meth
    fnum = int(e.get())
    meth = 'd'
    allclear()


# define the buttons

b1 = Button(root, text = "1", padx = 20, pady = 10, foreground = "white", bg = "black", activebackground = "grey",  command = lambda: myclick(1))
b2 = Button(root, text = "2", padx = 20, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: myclick(2))
b3 = Button(root, text = "3", padx = 20, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: myclick(3))

b4 = Button(root, text = "4", padx = 20, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: myclick(4))
b5 = Button(root, text = "5", padx = 20, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: myclick(5))
b6 = Button(root, text = "6", padx = 20, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: myclick(6))

b7 = Button(root, text = "7", padx = 20, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: myclick(7))
b8 = Button(root, text = "8", padx = 20, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: myclick(8))
b9 = Button(root, text = "9", padx = 20, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: myclick(9))

b0 = Button(root, text = "0", padx = 20, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: myclick(0))
bc = Button(root, text = "C", padx = 19, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: clear())
bac = Button(root, text = "AC", padx = 15, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: allclear())
be = Button(root, text = "=", padx = 100, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: equal())

ba = Button(root, text = "+", padx = 18, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: add())
bs = Button(root, text = "-", padx = 19, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: sub())
bm = Button(root, text = "*", padx = 19, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: mul())
bd = Button(root, text = "/", padx = 19, pady = 10, foreground = "white", bg = "black", activebackground = "grey", command = lambda: div())



# arrange the buttons into the grid

b1.grid(row = 3, column =0)
b2.grid(row = 3, column =1)
b3.grid(row = 3, column =2)

b4.grid(row = 2, column =0)
b5.grid(row = 2, column =1)
b6.grid(row = 2, column =2)

b7.grid(row = 1, column =0)
b8.grid(row = 1, column =1)
b9.grid(row = 1, column =2)

b0.grid(row = 4, column = 0)
bc.grid(row = 4, column = 1)
bac.grid(row = 4, column = 2)


ba.grid(row = 1, column = 3)
bs.grid(row = 2, column = 3)
bm.grid(row = 3, column = 3)
bd.grid(row = 4, column = 3)
be.grid(row = 5, column = 0, columnspan = 4)


# call the main function

root.mainloop()