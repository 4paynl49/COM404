from tkinter import *

##This is a test portion 
#class Gui(Tk):
    #pass

class Gui(Tk):

 # initialise window
  def __init__(self):
    super().__init__()

    # set window attributes
    #self.geometry("500x500")
    self.title("Gui")
    self.configure(bg="#eee",
                   height=500, 
                   width=500)
                
    # add window components by
    # ...creating an object of the component stored in an attribute
    self.heading_label = Label()
    self.heading_label.place(x=0, y=0)

    # ...setting the attributes of the component using the attribute
    self.heading_label.configure(font="Arial 24",
                                 text="This is a heading.")
    # ...assigning any event handlers to the component

  # handle events
  # (callback functions to handle events will go here)