#import Board #if you use this use Board.Board to access the object
from Board import Board

DEFAULTWIDTH = 8
DEFAULTHEIGHT = 8
DEFAULTNOOFMINES = 10

#Remember to use the object and not the module
class WebBoard(Board):
    def __init__(self):
        Board.__init__(self, DEFAULTWIDTH, DEFAULTHEIGHT, DEFAULTNOOFMINES)
        
