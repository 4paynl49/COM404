from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_subscribe_button()
        self.__add_mail_image_label()

        # load resources
        self.mail_image = PhotoImage(file="C:/Uni Repo/COM404/AE2 - Review TCA 1/Task A1/Mail.gif")
       

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.pack(fill=X)
        self.outer_frame.configure( bg="#eee", 
                                    padx=10, 
                                    pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.pack(fill=X)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 18",
                                        text="RECEIVE OUR NEWSLETTER")

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.pack(fill=X)
        self.instruction_label.configure(   bg="#eee",
                                            text="Please enter your email below to receiver our newsletter")

    def __add_email_frame(self):
        self.email_frame = Frame(self.outer_frame)
        self.email_frame.pack(fill=X)

    def __add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        self.email_label.configure( padx = 20,
                                    pady=20,
                                    text="Email:")

    def __add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=LEFT)
        self.email_entry.configure(width=40)

     # load defualt image
    def __add_mail_image_label(self):
        self.mail_image = Label(self.outer_frame)
        self.mail_image.pack(side=LEFT)
        self.mail_image.configure(image=self.mail_image,
                                             height=10,
                                             width=10)


    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.pack(fill=X)
        self.subscribe_button.configure(bg="#fcc",
                                        text="Subscribe")


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	