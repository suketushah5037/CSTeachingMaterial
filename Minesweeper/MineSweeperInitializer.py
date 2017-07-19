import random
#In my class module name and class name are the same
from WebBoard import WebBoard

class MineSweeperInitializer:

    def __init__(self):
        #instantiating board object
        board = WebBoard()
        
        #initialize zone array with 10 random mine positions
        #[i][j] make a mine position

        #randrange - including 0 and not including 8: 0-7
        for mineposition in range(10):
            randomnumberi = random.randrange(0, 8)
            randomnumberj = random.randrange(0, 8)
            board.zoneArr[randomnumberi][randomnumberj].isAMine = True
        
