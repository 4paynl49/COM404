from tkinter import *

class Gui(Tk):

 # initialise window
  def __init__(self):
    super().__init__()


    self.title("Gui")
    self.configure(bg="#eee",
                   height=500, 
                   width=500)
                
    self.heading_label = Label()
    self.heading_label.place(x=0, y=0)

    self.heading_label.configure(font="Arial 24",
                                 text="This is a heading.")

    