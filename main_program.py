import sys
from dependencies import login,register,unknown_support
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


def vp_start_gui():
 ''' display window to user showing options 
       for login, signup and exit '''
    global val, w, root
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
def destroyall():
    root.destroy()

class New_Toplevel:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("284x192+640+140")
        top.title("Student Registration")



        self.lab38 = Label(top)
        self.lab38.place(relx=0.04, rely=0.16, height=50, width=256)
        self.lab38.configure(text='''Student Registration System''',font=24)
        self.lab38.configure(width=256)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.25, rely=0.47, height=26, width=64)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Signin''',command=login.vp_start_gui)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.49, rely=0.47, height=26, width=69)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(text='''Signup''',command=register.vp_start_gui)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.39, rely=0.68, height=26, width=51)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(command=exit)
        self.Button3.configure(text='''Quit''',fg="red")






if __name__ == '__main__':
    vp_start_gui()


