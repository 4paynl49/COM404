from tkinter import *
from tkinter import messagebox
#import re



class Gui(Tk):

 # initialise window
    def __init__(self):
        super().__init__()

        # set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc",height=200,width=400,
                                 padx=10, pady=10)
        # load resources
        self.default_image = PhotoImage(file="./mail.gif")
        self.valid_image = PhotoImage(file="./mail_green.gif")
        self.nonValid_image = PhotoImage(file="./mail_red.gif")

        # add components
        self.__add_outer_frame()
        self.__add_heading_lable()
        self.__add_instruction_lable()
        self.__add_email_lable()
        self.__add_email_entry()
        self.__add_subscribe_button()
        self.__add_mail_image_label()

        # create a outer frame
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee")
       

    # create a heading lable 
    def __add_heading_lable(self):
        self.heading_lable = Label(self.outer_frame)
        self.heading_lable.grid(row=0, column=0, columnspan=2)
        self.heading_lable.configure(font="Arial 16", pady=10,
                                    text="RECEIVE OUR NEWSLETTER")
    # create a instruction lable
    def __add_instruction_lable(self):
        self.instruction_lable = Label(self.outer_frame)
        self.instruction_lable.grid(row=1, column=0, sticky=W)
        self.instruction_lable.configure(font="Arial 10",padx=10, pady=10,
                                        text="Please enter your email below to receive our newsletter.")

    # create a email lable
    def __add_email_lable(self):
        self.email_lable = Label(self.outer_frame)
        self.email_lable.grid(row=2, column=0, stick=W)
        self.email_lable.configure( font="Arial 10",padx=10, pady=10,
                                    text="Email:")

    # create a email entry
    def __add_email_entry(self):
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.grid(row=2, column=0)
        self.email_entry.configure(fg="#f00",borderwidth=2, width=35)

        self.email_entry.bind("<KeyRelease>", self.__email_entry_input)

    def __email_entry_input(self, event):
        if len(self.email_entry.get()) == 0:
            self.mail_image_label.configure(image=self.nonValid_image)
        else:
            self.mail_image_label.configure(image=self.valid_image)

    # load defualt image
    def __add_mail_image_label(self):
         self.mail_image_label = Label(self.outer_frame)
         self.mail_image_label.grid(row=2, column=0, stick=E,padx=10)
         self.mail_image_label.configure(image=self.default_image,
                                             height=30,
                                             width=50)
 
    # create a subscribe button
    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=3, column=0, columnspan=2, sticky=N+E+S+W)
        self.subscribe_button.configure(bg="#fee",font="Arial 10", 
                                        text= "Subscribe")

        self.subscribe_button.bind("<ButtonRelease-1>", self.__subscribe_button_clicked)
        

    def __subscribe_button_clicked(self, event):
        addressToVerify = self.email_entry.get()
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

        if match == None:
            messagebox.showinfo("Newsletter", "Enter Valid email address please")
            
        else: 
            messagebox.showinfo("Newsletter", "Subscribed!")
            


  



  
# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	
