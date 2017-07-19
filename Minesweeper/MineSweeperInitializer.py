import random
#In my class module name and class name are the same
from WebBoard import WebBoard

class MineSweeperInitializer:

    def __init__(self):
        #instantiating board object
        #don't miss the self. here,else it is a normal variable not an instance
        self.board = WebBoard()
        
        #initialize zone array with 10 random mine positions
        #[i][j] make a mine position

        #randrange - including 0 and not including 8: 0-7
        for mineposition in range(10):
            randomnumberi = random.randrange(0, 8)
            randomnumberj = random.randrange(0, 8)
            self.board.zoneArr[randomnumberi][randomnumberj].isAMine = True

    #dont forget to mention self as the first parameter even if there are none
    def getBoard(self):
        return self.board    

    

#For testing, move it to a unit test       
#msBoard = MineSweeperInitializer()
#print(  msBoard.getBoard().getWidth() )
