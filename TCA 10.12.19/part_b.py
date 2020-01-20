from tkinter import *
from tkinter import messagebox




class Gui(Tk):

 # initialise window
    def __init__(self):
        super().__init__()

        # set window properties
        self.title("Letter to Santa")
        self.configure(bg="#f66", height=200, width=400, padx=15, pady=15)

        # load resources
        self.santa_image = PhotoImage(file="./santa.gif")
        self.unknown_image = PhotoImage(file="./unknown.gif")
        self.snowman_image = PhotoImage(file="./snowman.gif")
        self.elf_image = PhotoImage(file="./elf.gif")
        #self.reindeer_image = PhotoImage(file"./reindeer.gif")

        # add components
        self.__add_global_frame()
        self.__add_heading_lable()
        self.__add_name_label()
        self.__add_name_enrty()
        self.__add_santa_image_label()
        self.__add_letter_text_label()
        self.__add_post_button()
        self.__add_unknown_image_label()

    # create a outer frame
    def __add_global_frame(self):
        self.global_frame = Frame()
        self.global_frame.grid(row=0, column=0)
        self.global_frame.configure(bg="#f33", padx=5)

    # create heading lable
    def __add_heading_lable(self):
        self.heading_lable = Label(self.global_frame)
        self.heading_lable.grid(row=0, column=0, columnspan=3)
        self.heading_lable.configure(bg="#f33",fg="#fff",font="Arial 18", pady=5,text="Write to Santa!")

    # create name label
    def __add_name_label(self):
        self.name_label = Label(self.global_frame)
        self.name_label.grid(row=2, column=0)
        self.name_label.configure(bg="#f33",fg="#fff",font="Arial 12", pady=5, text="Your name:")

    #  create name entry
    def __add_name_enrty(self):
        self.name_entry = Entry(self.global_frame)
        self.name_entry.grid(row=2, column=1, columnspan=2)
        self.name_entry.configure(borderwidth=2, width=40)

    # create santa image
    def __add_santa_image_label(self):
        self.santa_image_label = Label(self.global_frame)
        self.santa_image_label.grid(row=3, column=0)
        self.santa_image_label.configure(bg="#f33", image=self.santa_image)

    # create text box
    def __add_letter_text_label(self):
        self.letter_text_label = Text(self.global_frame)
        self.letter_text_label.grid(row=3, column=1, columnspan=2)
        self.letter_text_label.configure(height="5", width="30")

    # create post button
    def __add_post_button(self):
        self.post_button = Button(self.global_frame)
        self.post_button.grid(row=5, column=0,columnspan=3, sticky=N+E+S+W, padx=5, pady=5)
        self.post_button.configure(bg="#ff0",font="Arial 12", text= "Post Letter")

    # post button action
        self.post_button.bind("<ButtonRelease-1>", self.__post_button_clicked)

    # Subscribe button action    
    def __post_button_clicked(self, event):
        if len(self.name_entry.get()) == 0:
            messagebox.showinfo("Oops", "Please fill in you name")
        elif len(self.letter_text_label.get(str)):
            messagebox.showinfo("Oops", "Please write your letter to Santa")
        else: 
            messagebox.showinfo("Sent!", "Your letter has been posted!")

     # load defualt image
    def __add_unknown_image_label(self):
        self.unknown_image_label = Label(self.global_frame)
        self.unknown_image_label.grid(row=4, column=0, columnspan=3,padx=10, pady=10)
        self.unknown_image_label.configure(image=self.unknown_image,height=40,width=50)

        # self.name_entry.bind("<KeyRelease>", self.__name_entry_input)

        # if self.name_entry.get()== str("Snowy"):
        #     self.mail_image_label.configure(image=self.snowman_image)

        # elif self.name_entry.get()== str("Elfie"):
        #      self.mail_image_label.configure(image=self.elf_image)

        # elif self.name_entry.get()== str("Rudolph"):
        #     self.mail_image_label.configure(image=self.elf_image)
        # else:
        #     self.unknown_image_label.configure(image=self.unknown_image)

    
















        # Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	