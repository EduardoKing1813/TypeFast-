from logging import root
from tkinter import *
from modules.root_widgets import RootWelcomeLabel

def main():
    #Root window init
    root = Tk()
    root.title("TypeFast!")
    root.geometry("400x300")
    root.resizable(width=False, height=False)
    
    welcome_label = RootWelcomeLabel(root)
    welcome_label.grid(0,0)
    
    #Main loop
    root.mainloop()
    
    
    
    
    
    
    
    pass


if __name__ == '__main__':
    main()