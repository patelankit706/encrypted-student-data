
import sys
from . import database as db

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

def login():
 ''' login using the details 
         entered by user'''
    db.logintask((top.ent38.get()).upper(),top.Entry2.get())
    root.destroy()

def vp_start_gui():
 '''show window in which user 
      can enter login credentials '''
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

        top.geometry("457x208+486+127")
        top.title("Login")
        top.configure(highlightcolor="black")



        self.ent38 = Entry(top)
        self.ent38.place(relx=0.39, rely=0.34,height=20, relwidth=0.32)
        self.ent38.configure(background="white")
        self.ent38.configure(font="TkFixedFont")
        self.ent38.configure(selectbackground="#c4c4c4")

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.39, rely=0.48,height=20, relwidth=0.32)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.18, rely=0.34, height=18, width=70)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Username''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.18, rely=0.48, height=18, width=70)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Password''')

        self.but38 = Button(top)
        self.but38.place(relx=0.39, rely=0.67, height=26, width=59)
        self.but38.configure(activebackground="#d9d9d9")
        self.but38.configure(text='''Login''',command=login)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.57, rely=0.67, height=26, width=66)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=root.destroy)
        self.Button1.configure(text='''Cancel''')



if __name__ == '__main__':
    vp_start_gui()

