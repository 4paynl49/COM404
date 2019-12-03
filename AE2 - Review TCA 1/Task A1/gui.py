from tkinter import *

class Gui(Tk):

 # initialise window
    def __init__(self):
        super().__init__()

        # set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc",height=200,width=400,
                                 padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_lable()
        self.__add_instruction_lable()
        self.__add_email_lable()

        # create a outer frame
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee")

    # create a heading lable 
    def __add_heading_lable(self):
        self.heading_lable = Label(self.outer_frame)
        self.heading_lable.grid(row=0, column=0, columnspan=2)
        self.heading_lable.configure( font="Arial 18", pady=10,
                                        text="RECEIVE OUR NEWSLETTER")
    # create a instruction lable
    def __add_instruction_lable(self):
        self.instruction_lable = Label(self.outer_frame)
        self.instruction_lable.grid(row=1, column=0, sticky=W)
        self.instruction_lable.configure( font="Arial 10",padx=10, pady=10,
                                        text="Please enter your email below to receive our newsletter.")

    # create a email lable
    def __add_email_lable(self):
        self.email_lable = Label(self.outer_frame)
        self.email_lable.grid(row=2, column=0)
        self.email_lable.configure( font="Arial 10",padx=10, pady=10,
                                        text="Email:")



    
    


# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	