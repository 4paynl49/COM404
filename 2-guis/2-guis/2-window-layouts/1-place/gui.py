from tkinter import *

class Gui(Tk):

 # initialise window
    def __init__(self):
        super().__init__()


        self.title("Newsletter")
        self.configure(bg="#eee",
                   height=200, 
                   width=400)

        self.add_heading_label()    
        self.add_sub_heading()        
        self.add_email_label()
        self.add_email_box()
        self.add_submit_button()
        self.add_canvas()

    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.place(x=30, y=10)

        self.heading_label.configure(font="Arial 18",
                                 text="RECEIVE OUR NEWSLETTER")
    def add_sub_heading(self):
        self.sub_heading = Label()
        self.sub_heading.place(x=20, y=50)

        self.sub_heading.configure(font="Arial 11",
                                 text="Please enter you email below to receive our newsletter.")
    def add_email_label(self):
        self.email_label = Label()
        self.email_label.place(x=30, y=70)

        self.email_label.configure(font="Arial 11",
                                 text="Email:")

    def add_email_box(self):
        self.add_email_box = Entry()
        self.add_email_box.place(x=90, y=70)

    def add_submit_button(self):
        self.add_submit_button = Button()
        self.add_submit_button.place(x=50, y=90)

        self.add_submit_button.configure(font="Arial 11",
                                 text="Subscribe:")
    
    def add_canvas(self):
        self.add_canvas = Canvas()
        self.add_canvas.place(x=50, y=90)

        self.add_canvas.configure(bg="#F0F8FF")
        
  
