# import from tkinter
from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.bus_image = PhotoImage(file="C:/Uni Repo/COM404/2-guis/2-guis/4-images/3-positioning/images/bus.gif")
        self.map_image = PhotoImage(file="C:/Uni Repo/COM404/2-guis/2-guis/4-images/3-positioning/images/map.gif")
        
        
        # set window attributes
        self.title("Gui")

         # set window attributes
        self.title("X,Y")
        self.configure(padx=10, pady=10)
        
        # add components
        self.add_heading_label()
        self.add_map_frame()
        self.add_map_image()
        self.add_bus_image()
        
      
        # create a heading label
    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)

        self.heading_label.configure(font="Arial 16",text="Bus Journey")

        # create a frame
    def add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.grid(row=1, column=0)

        self.map_frame.configure(width=400, height=400)

        # place map image in frame
    def add_map_image(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)

        self.map_image_label.configure(image=self.map_image)
        
        # place bus image in frame
    def add_bus_image(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=self.bus_image)
        self.bus_image_label.bind("<B1-Motion>", self.bus_move)

    def bus_move(self, event):
        #messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
        #messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))
        self.bus_image_label.place(x=event.x, y=event.y)
 


    
# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	