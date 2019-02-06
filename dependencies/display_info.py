import sys

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

info=()

def vp_start_gui():
 ''' display information of student
           in textbox  '''
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


class New_Toplevel:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("368x432+665+140")
        top.title("Welcome")



        self.Text1 = Text(top)
        self.Text1.place(relx=0.03, rely=0.19, relheight=0.7, relwidth=0.94)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(width=346)
        self.Text1.configure(wrap=WORD)
        self.Text1.insert(END,'''Name  : %s

Rollno : %s

Mobile : %s

Sex    : %s

City   : %s'''%(info))

        self.Label1 = Label(top)
        self.Label1.place(relx=0.22, rely=0.02, height=48, width=176)
        self.Label1.configure(text='''Student Details''',font=24)
        self.Label1.configure(width=176)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.38, rely=0.9, height=26, width=77)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=root.destroy)
        self.Button1.configure(text='''Sign out''')






if __name__ == '__main__':
    vp_start_gui()
