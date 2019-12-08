from tkinter import *


class Gui(Tk):

 # initialise window
    def __init__(self):
        super().__init__()

# set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc",height=200,width=400,
                                 padx=10, pady=10)

        self.__add_mail_image_label()
        
        

    # load resources
        self.mail_image = PhotoImage(file="C:/Uni Repo/COM404/AE2 - Review TCA 1/Task A1/Mail.gif")
        


 # load defualt image
    def __add_mail_image_label(self):
        self.mail_image = Label()
        self.mail_image.grid(row=3, column=0)
        self.mail_image.configure(image=self.mail_image,
                                                  height=60,
                                                  width=60)

  

  
# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	