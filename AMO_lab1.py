from tkinter import *
from PIL import Image, ImageTk
import algs

def but_result1():
    """Shows results of the algorithm 1 or error message."""

    global l1

    # check for input errors
    try:
        _a = int(ent_a1.get())
        _b = int(ent_b1.get())
        _c = int(ent_c1.get())
        _d = int(ent_d1.get())
        _x = int(ent_x1.get())
        if _a == '' or _b == '' or _c == '' or _d == '' or _x == '':
            _res = 'You must fill in all the fields!'
        else:
            _res = algs.alg10(int(_a), int(_b), int(_c), int(_d), int(_x))
    except: _res = 'There are non-numeric symbols in your input.'

    # determination of the coordinates on which the result will appear
    if len(str(_res)) < 15: # no errors
        _c = 4
        _r = 7
        _cs = 3
    else:
        _c = 3
        _r = 8
        _cs = 7

    try:
        l1.destroy()
    finally:
        l1 = Label(root, text=_res, font=main_font, bg=bg_color1)
        l1.grid(column=_c, row=_r, columnspan=_cs, sticky=W)


def but_result2():
    """Shows results of the algorithm 2 or error message."""

    global l2

    # check for input errors
    try:
        _x = int(ent_x2.get())
        _y = int(ent_y2.get())
        _z = int(ent_z2.get())

        if _x == '' or _y == '' or _z == '':
            _res = 'You must fill in all the fields!'
        else:
            _res = algs.alg20(int(_x), int(_y), int(_z))
    except: _res = 'There are non-numeric symbols in your input.'

    # determination of the coordinates on which the result will appear
    if len(str(_res)) < 15: # no errors
        _c = 4
        _r = 7
        _cs = 3
    else:
        _c = 3
        _r = 8
        _cs = 7

    try:
        l2.destroy()
    finally:
        l2 = Label(root, text=f'y={_res}', font=main_font, bg=bg_color2)
        l2.grid(column=_c, row=_r, columnspan=_cs, sticky=W)


def but_result3():
    """Shows results of the algorithm 3 or error message."""

    global l3

    # check for input errors
    try:
        _a = int(ent_a3.get())
        _b = int(ent_b3.get())
        _n = int(ent_n3.get())
        if _a == '' or _b == '' or _n == '':
            _res = 'You must fill in all the fields!'
        else:
            _res = algs.alg30(int(_a), int(_b), int(_n))
    except: _res = 'There are non-numeric symbols in your input.'

    # determination of the coordinates on which the result will appear
    if len(str(_res)) < 15: # no errors
        _c = 4
        _r = 7
        _cs = 3
    else:
        _c = 3
        _r = 8
        _cs = 7

    try:
        l3.destroy()
    finally:
        l3 = Label(root, text=_res, font=main_font, bg=bg_color3)
        l3.grid(column=_c, row=_r, columnspan=_cs, sticky=W)


def show_flowchart1():
    """Shows block diagram of a linear algorithm in new Toplevel window."""

    _flowchart1 = PhotoImage(file=r"C:\Users\User\PycharmProjects\pythonProject8\test.png")

    slave1 = Toplevel(root)
    slave1.focus_set()
    slave1.title('Flowchart 1')

    _l1 = Label(slave1, image=_flowchart1)
    _l1.image = _flowchart1
    _l1.place(x=0, y=0, relwidth=1, relheight=1)

    _w = _flowchart1.width()
    _h = _flowchart1.height()
    slave1.geometry('%dx%d+0+0' % (_w, _h))
    slave1.resizable(width=False, height=False)


def show_flowchart2():
    """Shows block diagram of branching algorithm in new Toplevel window."""

    _flowchart2 = PhotoImage(file=r"C:\Users\User\PycharmProjects\pythonProject8\test.png")

    slave2 = Toplevel(root)
    slave2.focus_set()
    slave2.title('Flowchart 2')

    _l1 = Label(slave2, image=_flowchart2)
    _l1.image = _flowchart2
    _l1.place(x=0, y=0, relwidth=1, relheight=1)

    _w = _flowchart2.width()
    _h = _flowchart2.height()
    slave2.geometry('%dx%d+0+0' % (_w, _h))
    slave2.resizable(width=False, height=False)


def show_flowchart3():
    """Shows block diagram of a cyclic algorithm in new Toplevel window."""

    _flowchart3 = PhotoImage(file=r"C:\Users\User\PycharmProjects\pythonProject8\test.png")

    slave3 = Toplevel(root)
    slave3.focus_set()
    slave3.title('Flowchart 3')

    _l1 = Label(slave3, image=_flowchart3)
    _l1.image = _flowchart3
    _l1.place(x=0, y=0, relwidth=1, relheight=1)

    _w = _flowchart3.width()
    _h = _flowchart3.height()
    slave3.geometry('%dx%d+0+0' % (_w, _h))
    slave3.resizable(width=False, height=False)


def but1_bind():
    root.geometry('1150x680')
    root["bg"] = "yellow"

    global ent_a1, ent_b1, ent_c1, ent_d1, ent_x1

    Label(root, text='', font='Calibri 14', width=80, height=25, bg="yellow")\
        .grid(row=0, column=1, rowspan=12, columnspan=10)

    Label(root, text='a', justify=RIGHT, font=main_font, bg="yellow").grid(column=2, row=1, sticky=E)
    Label(root, text='b', justify=RIGHT, font=main_font, bg="yellow").grid(column=2, row=3, sticky=E)
    Label(root, text='c', justify=RIGHT, font=main_font, bg="yellow").grid(column=2, row=5, sticky=E)
    Label(root, text='d', justify=RIGHT, font=main_font, bg="yellow").grid(column=6, row=1, sticky=E)
    Label(root, text='x', justify=RIGHT, font=main_font, bg="yellow").grid(column=6, row=3, sticky=E)

    ent_a1 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_b1 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_c1 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_d1 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_x1 = Entry(root, font='Calibri 14', width=10, bd=0)

    ent_a1.grid(column=3, row=1, columnspan=2, sticky=W, padx=5)
    ent_b1.grid(column=3, row=3, columnspan=2, sticky=W, padx=5)
    ent_c1.grid(column=3, row=5, columnspan=2, sticky=W, padx=5)
    ent_d1.grid(column=7, row=1, columnspan=2, sticky=W, padx=5)
    ent_x1.grid(column=7, row=3, columnspan=2, sticky=W, padx=5)

    Button(root, text='Result', font=main_font, bg='chartreuse2', command=but_result1).grid(column=3, row=7)
    Button(root, text='Show flowchart', font=main_font, bg='chartreuse2', command=show_flowchart2)\
        .grid(column=6, row=7, columnspan=3)

def but2_bind():
    """Appear fields to determine the variables of the algorithm 2."""

    root.geometry('1150x680')
    global ent_x2, ent_y2, ent_z2
    root["bg"] = "yellow"

    Label(root, text='', font='Calibri 14', width=80, height=25, bg="yellow")\
        .grid(row=0, column=1, rowspan=12, columnspan=10)

    Label(root, text='x', justify=RIGHT, font=main_font, bg="yellow").grid(column=2, row=1, sticky=E)
    Label(root, text='y', justify=RIGHT, font=main_font, bg="yellow").grid(column=2, row=3, sticky=E)
    Label(root, text='z', justify=RIGHT, font=main_font, bg="yellow").grid(column=2, row=5, sticky=E)

    ent_x2 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_y2 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_z2 = Entry(root, font='Calibri 14', width=10, bd=0)

    ent_x2.grid(column=3, row=1, columnspan=2, sticky=W, padx=5)
    ent_y2.grid(column=3, row=3, columnspan=2, sticky=W, padx=5)
    ent_z2.grid(column=3, row=5, columnspan=2, sticky=W, padx=5)

    Button(root, text='Result', font=main_font, bg='chartreuse2', command=but_result2).grid(column=3, row=7)
    Button(root, text='Show flowchart', font=main_font, bg='chartreuse2', command=show_flowchart2)\
        .grid(column=6, row=7, columnspan=3)


def but3_bind():
    root.geometry('1150x680')
    global ent_a3, ent_b3, ent_n3
    root["bg"] = "yellow"

    Label(root, text='', font='Calibri 14', width=80, height=25, bg="yellow")\
        .grid(row=0, column=1, rowspan=12, columnspan=10)

    Label(root, text='a', justify=RIGHT, font=main_font, bg="yellow").grid(column=2, row=1, sticky=E)
    Label(root, text='b', justify=RIGHT, font=main_font, bg="yellow").grid(column=2, row=3, sticky=E)
    Label(root, text='n', justify=RIGHT, font=main_font, bg="yellow").grid(column=2, row=5, sticky=E)

    ent_a3 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_b3 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_n3 = Entry(root, font='Calibri 14', width=10, bd=0)

    ent_a3.grid(column=3, row=1, columnspan=2, sticky=W, padx=5)
    ent_b3.grid(column=3, row=3, columnspan=2, sticky=W, padx=5)
    ent_n3.grid(column=3, row=5, columnspan=2, sticky=W, padx=5)

    Button(root, text='Result', font=main_font, bg='chartreuse2', command=but_result3).grid(column=3, row=7)
    Button(root, text='Show flowchart', font=main_font, bg='chartreuse2', command=show_flowchart2)\
        .grid(column=6, row=7, columnspan=3)


if __name__ == '__main__':
    root = Tk()
    root.title('Main window')
    root.resizable(width=False, height=False)
    root.geometry('370x680')

    # set background
    bg_color1 = 'red'
    bg_color2 = 'green'
    bg_color3 = 'blue'
    main_font = 'Verdana 14'

    # main buttons
    photo1 = PhotoImage(file=r"C:\Users\User\PycharmProjects\pythonProject8\picslab1\alg1.png")
    photo2 = PhotoImage(file=r"C:\Users\User\PycharmProjects\pythonProject8\picslab1\alg2.png")
    photo3 = PhotoImage(file=r"C:\Users\User\PycharmProjects\pythonProject8\picslab1\alg3.png")

    Button(root, compound=BOTTOM, image=photo1, bd=0, text='Algorithm 1\n', relief=GROOVE, width=370, height=190,
           font='Verdana 16 bold', bg=bg_color1, activebackground=bg_color1, command=but1_bind)\
        .grid(column=0, row=0, rowspan=4,)

    Button(root, compound=BOTTOM, image=photo2, bd=0, text='Algorithm 2\n', relief=GROOVE, width=370, height=300,
           font='Verdana 16 bold', bg=bg_color2, activebackground=bg_color2, command=but2_bind)\
        .grid(column=0, row=4, rowspan=4,)

    Button(root, compound=BOTTOM, image=photo3, bd=0, text='Algorithm 3\n', relief=GROOVE, width=370, height=190,
           font='Verdana 16 bold', bg=bg_color3, activebackground=bg_color3, command=but3_bind)\
        .grid(column=0, row=8, rowspan=4,)

    root.mainloop()
