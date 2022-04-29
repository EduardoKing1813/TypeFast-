from this import d
from tkinter import Label


class RootWidget:
    
    def grid(self, r, c):
        self.widget.grid(row=r, column=c)


class RootWelcomeLabel(RootWidget):
    
    def __init__(self, root):
        self.root = root
        self.widget = Label(root, text="TypeFast!")
        
        
