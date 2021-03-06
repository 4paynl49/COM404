from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.pickle_image = PhotoImage(file="C:/Uni Repo/COM404/2-guis/2-guis/5-animation/1-single-object/pickle.gif")
        
        # set window attributes
        self.title("Pickle bounce")
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.pickle_x_pos = 250
        self.pickle_y_pos = 0
        self.pickle_x_change = 1
        self.pickle_y_change = 1
        #self.pickle_x_change1 = -1
        #self.pickle_y_change1 = -1

        # add components
        self.add_pickle_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):

        if  self.pickle_x_pos > 450:
            self.pickle_x_change = -1

        if  self.pickle_y_pos > 384:
            self.pickle_y_change = -1

        if  self.pickle_x_pos < 0:
            self.pickle_x_change = 1

        if  self.pickle_y_pos < 0:
            self.pickle_y_change = 1
   
        self.pickle_x_pos = self.pickle_x_pos + self.pickle_x_change

        self.pickle_y_pos = self.pickle_y_pos + self.pickle_y_change
        self.pickle_image_label.place(x=self.pickle_x_pos, 
                                    y=self.pickle_y_pos)
        self.after(50, self.tick)

    

    # the pickle image
    def add_pickle_image_label(self):
        self.pickle_image_label = Label()
        self.pickle_image_label.place(x=self.pickle_x_pos,
                                    y=self.pickle_y_pos)
        self.pickle_image_label.configure(image=self.pickle_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 