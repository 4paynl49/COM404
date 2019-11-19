from tkinter import *
class Gui(Tk):
   
    def __init__(self):
        super().__init__()
       
        # set window attributes
        self.title("Song Maker")
       
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_lyric_frame()
        self.__add_lyric_entry()
        self.__add_lyric_button()
        self.__add_lyric_label()
         
    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        #style
        self.heading_label.configure(font="Arial 16",
                                        text="Song Maker")
    def __add_instruction_label(self):
        #create
        self.instruction_label= Label()
        self.instruction_label.grid(row=1, column=0)
        #style
        self.instruction_label.configure(font="Arial 11",
                                        text="Lyrics to add:")
    def __add_lyric_frame(self):
        self.lyric_frame = Frame()
        self.lyric_frame.grid(row=2, column=0)
    def __add_lyric_entry(self):
        #create
        self.lyric_entry= Entry(self.lyric_frame)
        self.lyric_entry.pack(side=LEFT)
    def __add_lyric_button(self):
        # create
        self.lyric_button = Button(self.lyric_frame)
        self.lyric_button.pack(side=RIGHT)
        self.lyric_button.configure(text="Add:")
    def __add_lyric_label(self):
        #create
        self.lyric_label= Label()
        self.lyric_label.grid(row=3, column=0)
        #style
        self.lyric_label.configure(font="Arial 11",
                                        text="Lyrics:")