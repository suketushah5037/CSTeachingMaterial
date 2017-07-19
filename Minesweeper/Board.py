#Just the class defining the Board, the rule engine is the Mineweeper.js
#The UI uses the Board to display
import Zone

DEFAULTWIDTH = 8
DEFAULTHEIGHT = 8
DEFAULTNOOFMINES = 10


class Board:
    width = DEFAULTWIDTH
    height = DEFAULTHEIGHT
    noofmines = DEFAULTNOOFMINES
    noofminesleft = DEFAULTNOOFMINES
    zoneArr = [[Zone.Zone() for i in range(DEFAULTWIDTH)] for j in range(DEFAULTHEIGHT)]

    #constructor
    def __init__(self, width, height, noofmines):
        self.width = width
        self.height = height
        self.noofmines = noofmines
        #Initially it is the same as the number of mines
        self.noofminesleft =  noofmines
        #Two dimensional array of Zones using list comprehension
        self.zoneArr = [[Zone.Zone() for i in range(self.width)] for j in range(self.height)]
        

