from tkinter import *
from PIL import Image, ImageTk
import algs


def but_result1():
    """Shows results of the algorithm 1 or error message."""

    global l1

    # check for input errors
    try:
        _a = ent_a1.get()
        _b = ent_b1.get()
        _c = ent_c1.get()
        if _a == '' or _b == '' or _c == '':
            _res = 'You must fill in all the fields!'
        else:
            _res = round(algs.alg1(int(_a), int(_b), int(_c)), 3)
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
        _b = int(ent_b2.get())
        _z = int(ent_z2.get())
        _d = int(ent_d2.get())
        _w = int(ent_w2.get())
        _f = int(ent_f2.get())
        if _b == '' or _z == '' or _d == '' or _w == '' or _f == '':
            _res = 'You must fill in all the fields!'
        else:
            _res = round(algs.alg2(int(_b), int(_z), int(_d), int(_w), int(_f)), 3)
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
        l2 = Label(root, text=_res, font=main_font, bg=bg_color2)
        l2.grid(column=_c, row=_r, columnspan=_cs, sticky=W)


def but_result3():
    """Shows results of the algorithm 3 or error message."""

    global l3

    # check for input errors
    try:
        _a = int(ent_a3.get())
        _b = int(ent_b3.get())
        if _a == '' or _b == '':
            _res = 'You must fill in all the fields!'
        else:
            _res = round(algs.alg3(int(_a), int(_b)), 3)
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

    _flowchart1 = PhotoImage(file=r"C:\Users\User\OneDrive\Робочий стіл\my first html\images\images.jpg")

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

    _flowchart2 = PhotoImage(file=r"C:\Users\User\OneDrive\Робочий стіл\my first html\images\images.jpg")

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

    _flowchart3 = PhotoImage(file=r"C:\Users\User\OneDrive\Робочий стіл\my first html\images\images.jpg")

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
    """Appear fields to determine the variables of the algorithm 1."""

    global ent_a1, ent_b1, ent_c1
    root.geometry('1150x570')

    Label(root, text='', font='Calibri 14', width=80, height=25, bg=bg_color1)\
        .grid(row=0, column=1, rowspan=12, columnspan=10)

    Label(root, text='a', justify=RIGHT, font=main_font, bg=bg_color1).grid(column=2, row=1, sticky=E)
    Label(root, text='b', justify=RIGHT, font=main_font, bg=bg_color1).grid(column=2, row=3, sticky=E)
    Label(root, text='c', justify=RIGHT, font=main_font, bg=bg_color1).grid(column=2, row=5, sticky=E)

    ent_a1 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_b1 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_c1 = Entry(root, font='Calibri 14', width=10, bd=0)

    ent_a1.grid(column=3, row=1, columnspan=2, sticky=W, padx=5)
    ent_b1.grid(column=3, row=3, columnspan=2, sticky=W, padx=5)
    ent_c1.grid(column=3, row=5, columnspan=2, sticky=W, padx=5)

    Button(root, text='Result', font=main_font, bg='deep sky blue', command=but_result1).grid(column=3, row=7)
    Button(root, text='Show flowchart', font=main_font, bg='deep sky blue', command=show_flowchart1)\
        .grid(column=6, row=7, columnspan=3)


def but2_bind():
    """Appear fields to determine the variables of the algorithm 2."""

    global ent_b2, ent_z2, ent_d2, ent_w2, ent_f2
    root.geometry('1150x570')

    Label(root, text='', font='Calibri 14', width=80, height=25, bg=bg_color2)\
        .grid(row=0, column=1, rowspan=12, columnspan=10)

    Label(root, text='b', justify=RIGHT, font=main_font, bg=bg_color2).grid(column=2, row=1, sticky=E)
    Label(root, text='z', justify=RIGHT, font=main_font, bg=bg_color2).grid(column=2, row=3, sticky=E)
    Label(root, text='d', justify=RIGHT, font=main_font, bg=bg_color2).grid(column=2, row=5, sticky=E)
    Label(root, text='w', justify=RIGHT, font=main_font, bg=bg_color2).grid(column=6, row=1, sticky=E)
    Label(root, text='f', justify=RIGHT, font=main_font, bg=bg_color2).grid(column=6, row=3, sticky=E)

    ent_b2 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_z2 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_d2 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_w2 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_f2 = Entry(root, font='Calibri 14', width=10, bd=0)

    ent_b2.grid(column=3, row=1, columnspan=2, sticky=W, padx=5)
    ent_z2.grid(column=3, row=3, columnspan=2, sticky=W, padx=5)
    ent_d2.grid(column=3, row=5, columnspan=2, sticky=W, padx=5)
    ent_w2.grid(column=7, row=1, columnspan=2, sticky=W, padx=5)
    ent_f2.grid(column=7, row=3, columnspan=2, sticky=W, padx=5)

    Button(root, text='Result', font=main_font, bg='chartreuse2', command=but_result2).grid(column=3, row=7)
    Button(root, text='Show flowchart', font=main_font, bg='chartreuse2', command=show_flowchart2)\
        .grid(column=6, row=7, columnspan=3)


def but3_bind():
    """Appear fields to determine the variables of the algorithm 3."""

    global ent_a3, ent_b3
    root.geometry('1150x570')

    Label(root, text='', font='Calibri 14', width=80, height=25, bg=bg_color3)\
        .grid(row=0, column=1, rowspan=12, columnspan=10)

    Label(root, text='a', justify=RIGHT, font=main_font, bg=bg_color3).grid(column=2, row=1, sticky=E)
    Label(root, text='b', justify=RIGHT, font=main_font, bg=bg_color3).grid(column=2, row=3, sticky=E)

    ent_a3 = Entry(root, font='Calibri 14', width=10, bd=0)
    ent_b3 = Entry(root, font='Calibri 14', width=10, bd=0)

    ent_a3.grid(column=3, row=1, columnspan=2, sticky=W, padx=5)
    ent_b3.grid(column=3, row=3, columnspan=2, sticky=W, padx=5)

    Button(root, text='Result', font=main_font, bg='orange', command=but_result3).grid(column=3, row=7)
    Button(root, text='Show flowchart', font=main_font, bg='orange', command=show_flowchart3)\
        .grid(column=6, row=7, columnspan=3)


if __name__ == '__main__':
    root = Tk()
    root.title('Main window')
    root.resizable(width=False, height=False)
    root.geometry('370x570')

    # set background
    bg_color1 = 'sky blue'
    bg_color2 = 'green yellow'
    bg_color3 = 'gold'
    main_font = 'Verdana 14'


    def factorial(x):
        if x < 0:
            raise ValueError
        else:
            res = 1
            for i in list(range(x)):
                res = res * (i + 1)
            return res


    def alg1(a, b, c):
        return (a * c) ** 2 + (b * c) ** 3 + c ** 8


    def alg2(b, z, d, w, f):
        from math import sin, cos

        if z == 0:
            return 'ZeroDivisonError. Check your input.'
        elif b / z > d:
            return sin(w * f)
        else:
            return cos(w * f)


    def alg3(a, b):
        if a - b < 0:
            return 'a-b < 0. Enable to calculate (a-b)!.\n' \
                   'Check your input.'
        else:
            return factorial(a) * b / factorial(a - b)


    # main buttons
    photo1 = PhotoImage(file=r"C:\Users\User\PycharmProjects\pythonProject8\test.png")
    photo2 = PhotoImage(file=r"C:\Users\User\PycharmProjects\pythonProject8\test.png")
    photo3 = PhotoImage(file=r"C:\Users\User\PycharmProjects\pythonProject8\test.png")

    Button(root, compound=BOTTOM, image=photo1, bd=0, text='Algorithm 1\n', relief=GROOVE, width=370, height=190,
           font='Verdana 16 bold', bg=bg_color1, activebackground=bg_color1, command=but1_bind)\
        .grid(column=0, row=0, rowspan=4,)

    Button(root, compound=BOTTOM, image=photo2, bd=0, text='Algorithm 2\n', relief=GROOVE, width=370, height=190,
           font='Verdana 16 bold', bg=bg_color2, activebackground=bg_color2, command=but2_bind)\
        .grid(column=0, row=4, rowspan=4,)

    Button(root, compound=BOTTOM, image=photo3, bd=0, text='Algorithm 3\n', relief=GROOVE, width=370, height=190,
           font='Verdana 16 bold', bg=bg_color3, activebackground=bg_color3, command=but3_bind)\
        .grid(column=0, row=8, rowspan=4,)

    root.mainloop()
