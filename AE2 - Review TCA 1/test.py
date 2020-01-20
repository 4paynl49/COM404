from tkinter import *


class Gui(Tk):

 # initialise window
    def __init__(self):
        super().__init__()

# set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc",height=200,width=400,
                                 padx=10, pady=10)

        self.__add_outer_frame()
        self.__add_sub_type_optionMenu()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee")

    def __add_sub_type_optionMenu(self):

        # dictionary with options
        subPeriod = ["Weekly","Monthly","Yearly"]
        
        # set selected entry
        selectPeriod = StringVar()
        selectPeriod.set(subPeriod[0])

        self.sub_type_optionMenu = OptionMenu(self.outer_frame, selectPeriod, *subPeriod)
        self.sub_type_optionMenu.grid(row=3, column=0, padx=10, pady=10)
        self.sub_type_optionMenu.configure(fg="#f00",borderwidth=2, width=35)

    # def __add_test():
    #     print "value is", selectPeriod.get()

       
  
# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	