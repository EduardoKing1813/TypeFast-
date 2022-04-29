from tkinter import *
from modules.root_widgets import RootWelcomeLabel, SettingsFrame

def main():
    #Root window init
    root = Tk()
    root.title("TypeFast!")
    #root.geometry("400x300")
    root.resizable(width=False, height=False)
    
    welcome_label = RootWelcomeLabel(root)
    welcome_label.grid(row=0, column=1)
    
    settings_frame = SettingsFrame(root)
    settings_frame.grid(row=1, column=0)
    
    #Main loop
    root.mainloop()



if __name__ == '__main__':
    main()