from tkinter import Label, Radiobutton
from tkinter.ttk import LabelFrame, Combobox


class RootWidget:
    
    def grid(self, row, column):
        self.widget.grid(row=row, column=column)


class RootWelcomeLabel(RootWidget):
    
    def __init__(self, root):
        self.root = root
        self.widget = Label(root, text="TypeFast!")
        
        
class SettingsFrame(RootWidget):
    
    def __init__(self, root):
        self.root = root
        
        #Creating widget body
        self.widget = LabelFrame(root, text="Settings")
        
        #Widgets for text seletion
        self.label_text = Label(self.widget, text="Text:")
        self.label_text.grid(row=0, column=0, sticky="W")
        
        self.combobox_text_selection = Combobox(self.widget)
        self.combobox_text_selection['values'] = ['a', 'b', 'c']
        self.combobox_text_selection.grid(row=1, column=0, pady=(0, 30))
        
        #Widgets for case sensitivity selection
        self.label_case_sensitivity_selection = Label(self.widget, text="Is case sensitive:")
        self.label_case_sensitivity_selection.grid(row=2, column=0, sticky="W")
        
        self.radio_buttons_case_sensitivity_selection_items = {"Yes" : True, "No (easy)" : False}
        self.radio_buttons_case_sensitivity_selection = []
        
        for (text, value) in self.radio_buttons_case_sensitivity_selection_items.items():
            self.radio_buttons_case_sensitivity_selection.append( Radiobutton(self.widget, text=text, value=value) )
        
        for index, rb in enumerate(self.radio_buttons_case_sensitivity_selection):
            rb.grid(row=3, column=index, sticky="W", pady=(0, 30))
            
        #Widgets for color selection
        self.label_color_selection = Label(self.widget, text="Next character color:")
        self.label_color_selection.grid(row=4, column=0, sticky="W")
        
        self.combobox_color_selection = Combobox(self.widget)
        self.combobox_color_selection['values'] = ['Red', 'Green', 'Blue']
        self.combobox_color_selection.grid(row=5, column=0, sticky="W", pady=(0, 60))
        
        
        
        