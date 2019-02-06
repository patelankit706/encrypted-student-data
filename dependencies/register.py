
import sys
from . import database
from .encrypt import xorWord as xor,encrypt
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from . import unknown_support

def register():
 ''' enter encrypted data in database '''    database.insertStud(xor(top.Entry1.get().upper(),"cyberry"),xor(top.Entry2.get().upper(),top.Entry3.get()),encrypt(top.Entry3.get()),xor(top.Entry4.get().upper(),top.Entry3.get()),xor(top.Entry5.get().upper(),top.Entry3.get()),xor(top.Entry6.get().upper(),top.Entry3.get()))
    root.destroy()

def vp_start_gui():
 '''show window to user for entering 
      registration information '''
    global val, w, root,top
    root = Tk()
    top = New_Toplevel (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("380x450+640+140")
        top.title("Register")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.24, rely=0.04, height=38, width=156)
        self.Label1.configure(text='''Registration Form''')
        self.Label1.configure(width=156)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.47, rely=0.22,height=20, relwidth=0.38)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.47, rely=0.33,height=20, relwidth=0.38)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.47, rely=0.44,height=20, relwidth=0.38)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")

        self.Label2 = Label(top)
        self.Label2.place(relx=0.08, rely=0.22, height=18, width=130)
        self.Label2.configure(text='''Roll No (Username)''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.24, rely=0.33, height=18, width=39)
        self.Label3.configure(text='''Name''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.21, rely=0.44, height=18, width=65)
        self.Label4.configure(text='''Password''')

        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.47, rely=0.56,height=20, relwidth=0.38)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")

        self.Label5 = Label(top)
        self.Label5.place(relx=0.21, rely=0.56, height=18, width=67)
        self.Label5.configure(text='''Mobile No''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.26, rely=0.67, height=18, width=26)
        self.Label6.configure(text='''Sex''')

        self.Entry5 = Entry(top)
        self.Entry5.place(relx=0.47, rely=0.76,height=20, relwidth=0.38)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")

        self.Label7 = Label(top)
        self.Label7.place(relx=0.26, rely=0.76, height=18, width=27)
        self.Label7.configure(text='''City''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.58, rely=0.89, height=26, width=66)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(text='''Cancel''',fg="red",command=root.destroy)

        self.Entry6 = Entry(top)
        self.Entry6.place(relx=0.47, rely=0.67,height=20, relwidth=0.38)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.24, rely=0.89, height=26, width=75)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Register''',command=register)






if __name__ == '__main__':
    vp_start_gui()
