import time

HIGHSCORES_PATH = 'highscores/highscores.txt'

class Highscore:
    
    @staticmethod
    def load() -> list:
        lst = []
        
        with open(HIGHSCORES_PATH) as f:
            for line in f:
                args = line.split(' - ')
                args[-1] = bool(args[-1]) #Convert string to boolean value
                lst.append( Highscore(*args) )
            
        return lst
            
    
    def __init__(self, time:time.time, name:str, text_name:str, is_case_sensitive):
        self.time = time
        self.name = name
        self.text_name = text_name
        self.is_case_sensitive = is_case_sensitive
        
    
    def __repr__(self) -> str:
        case_sensitive = 'CS' if self.is_case_sensitive else 'NCS'
        return f'{self.time} - {self.name} - {self.text_name} - {case_sensitive}'