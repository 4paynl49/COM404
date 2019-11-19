from tkinter import *

class Gui(Tk):

  # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#eee",
                        height=177, 
                        width=340)

        self.add_heading_label()
        self.addemailNewsletter()
        self.add_email_frame()
        self.addEmail()
        self.addemailBox()
        self.addsubscribeButton()  





    def add_heading_label(self):
        # create   
        self.heading_label = Label()
        self.heading_label.pack()

        # style
        self.heading_label.configure(font="Arial 14",
                                        text="RECEIVE OUR NEWSLETTER")

    def addemailNewsletter (self):
        # create
        self.emailNewsletter = Label()
        self.emailNewsletter.pack()

        #style
        self.emailNewsletter.configure(font="Arial 9",
                                    text="Please enter your email below to recieve our newsletter")


    def addEmail (self):
        # create
        self.Email = Label(self.email_frame)
        self.Email.pack(side=LEFT)

        #style
        self.Email.configure(font="Arial 9",
                                    text="Email:")

    def addemailBox (self):
        # create
        self.emailBox = Entry(self.email_frame)
        self.emailBox.pack(side=RIGHT)
        self.emailBox.configure(width=30)


    def addsubscribeButton (self):
        # create
        self.subscribeButton = Button()
        self.subscribeButton.pack()
        self.subscribeButton.configure(width=45)

        self.subscribeButton.configure(font="Arial 9",
                                    text="Subscribe")


    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack()