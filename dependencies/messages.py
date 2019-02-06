try:
  import Tkinter as tk
except ImportError:
  import tkinter as tk

try:
  import tkMessageBox as msg
except ImportError:
  import tkinter.messagebox as msg


class button:
  def __init__(self,message):
    self.message=message
  def b_info(self):
    msg.showinfo('Info',self.message)
  def b_error(self):
    msg.showwarning('Warning',self.message)
  def b_warn(self):
    msg.showerror('Error',self.message)

class no_button(button):
  def messageNoB(self):
    master=tk.Tk()
    master.title("Message")
    msg = tk.Message(master,aspect=400,padx=10,fg="grey", text = self.message)
    msg.config(font=('times', 11))
    msg.pack()
    tk.mainloop()
  


  
