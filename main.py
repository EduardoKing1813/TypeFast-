
from tkinter import *
from modules.highscore import Highscore
from modules.root_widgets import HighscoreFrame, RootWelcomeLabel, SettingsFrame, MiddleFrame


def on_button_start_click():
    pass


def main():
    #Root window init
    root = Tk()
    root.title("TypeFast!")
    #root.geometry("600x400")
    root.resizable(width=False, height=False)
    
    welcome_label = RootWelcomeLabel(root)
    welcome_label.grid(row=0, column=1)
    
    settings_frame = SettingsFrame(root)
    settings_frame.grid(row=1, column=0, sticky='NS')
    
    middle_frame = MiddleFrame(root, on_button_start_click)
    middle_frame.grid(row=1, column=1, sticky='NS')

    highscore_frame = HighscoreFrame(root)
    highscore_frame.grid(row=1, column=2, sticky='NS')
    
    
    highscores = Highscore.load()
    for item in highscores:
        print(item)
    
    #Main loop
    root.mainloop()



if __name__ == '__main__':
    main()