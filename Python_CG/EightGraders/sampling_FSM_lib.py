#sample FSM OOP
#Outside the library
#This is the hangman player who knows how many states are there and the state transitions

from functools import partial
import FSM_OOP
import random

#Notice the way, am starting, it is with the use case and then building up on the fsm and state classes
#constant to maintain max guesses
MAXGUESSES = 7
START, INITIALIZE, GUESS, END = 'START', 'INITIALIZE', 'GUESS', 'END'
TRSTART, TRINITIALIZE, TRGUESS, TREND = 'trstart', 'trinitialize', 'trguess', 'trend'
class CompPlayer:
    #class variable a lits of states
    states = [START, INITIALIZE, GUESS, END]
    def __init__(self, name):
        #named arguments - arguments are a dictionary
        #model is the player object
        #states is the class variable states, which must be the same for all players of hangman
        self.FSM = FSM_OOP.Machine(model=self, states=CompPlayer.states, initial=START)
        self.name = name
        #Any other hangman player can choose a different number of guesses for hiimself
        self.numberofguesses = MAXGUESSES
        
        #add transitions
        #Triggers are the strings on which player object is expected to 
        #change transitions
        self.FSM.add_transition(trigger='start_machine', source=START, dest=INITIALIZE, after=[self.trinitialize], conditions=[self.trstart])
        self.FSM.add_transition(trigger='start_machine', source=INITIALIZE, dest=GUESS, conditions=[self.trinitialize])
        self.FSM.add_transition(trigger='start_machine', source=GUESS, dest=GUESS, conditions=[self.trstart])
        #TODO: later change to, do you want to play again and restart
        self.FSM.add_transition(trigger='start_machine', source=GUESS, dest=END, conditions=[self.trstart])

    def trstart(self):
        #start the FSM
        #select a movie and pass it to initialize
        #TODO: handle spaces later
        #TODO: movie name is too long and you want to guess all at once without hanging
        #TODO: handle spaces later
        #TODO: movie name is too long and you want to guess all at once without hanging
        movielist = [ 'gonewiththewind', 'diehard', 'soundofmusic', 'breakfastattiffany''s']
        #range of one less than the last item - 0 to 3
        movieitem =  random.randint(0, len(movielist)-1)
        #the movie selected
        #only this is maintained in the state object
        self.selectedmovie = movielist[movieitem]
        
        #User message
        print("Are you ready for a game of hangman?")
        return True
    
    def trinitialize(self):
        print("selected movie = ", self.selectedmovie)
        return True
    
def run(player):
    """

    Returns:
        object: 
    """
    player.start_machine()
def main():
    #hangmanplayer is the name of the player
    player = CompPlayer("HangmanPlayer")
    #Notice the name of the trigger is a function name on the player object

    #print("calling trstart")
    run(player)


if __name__ == "__main__":
    main()
