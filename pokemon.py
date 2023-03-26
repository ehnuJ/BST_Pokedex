'''
Name: Joon Hee Ooten
Date: 11/11/2022
Pokemon class
'''

class Pokemon:
    def __init__(self, usa, ID, jp):
        self.usa = usa
        self.jp = jp
        self.ID = ID
    
    def __str__(self):
        return f'{self.usa} {self.jp} {self.ID}'
    
    def __eq__(self, thing):
        return self.ID == thing
    
    def __ne__(self, thing):
        return self.ID != thing
    
    def __lt__(self, thing):
        return self.ID < thing
    
    def __le__(self, thing):
        return self.ID <= thing
    
    def __gt__(self, thing):
        return self.ID > thing
    
    def __ge__(self, thing):
        return self.ID >= thing