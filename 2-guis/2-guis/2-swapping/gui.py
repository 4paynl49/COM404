from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.headphone_image = PhotoImage(file="C:/Uni Repo/COM404/2-guis/2-guis/2-swapping/Hair-Blow.gif")
        self.headphone_name_image = PhotoImage(file="C:/Uni Repo/COM404/2-guis/2-guis/2-swapping/Hair-Blow-text.gif")

        # set window attributes
        self.title("Gui")

         # set window attributes
        self.title("Swap")
        self.configure(padx=10, pady=10)
        
        # add components
        self.add_heading_label()
        self.add_headphone_label()
        self.add_flip_button()

    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=3)

        self.heading_label.configure(font="Arial 48",text="Headphones")

    def add_headphone_label(self):
        self.headphone_image_label = Label()
        self.headphone_image_label.grid(row=1, column=0)
        self.headphone_image_label.configure(image=self.headphone_image,
                                             height=400,
                                             width=600)
  
    def add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=3, column=0)

        self.flip_button.configure(font="Arial 16",text="Flip")
        self.flip_button.bind("<ButtonRelease-1>", self.left_button_clicked)
        self.flip_button.bind("<ButtonRelease-3>", self.right_button_clicked)

    def left_button_clicked(self, event):
        self.headphone_image_label.configure(image = self.headphone_image)

    def right_button_clicked(self, event):   
        self.headphone_image_label.configure(image = self.headphone_name_image)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	