from time import clock
import random
import re

START, INITIALIZE, GUESS = 'START', 'INITIALIZE', 'GUESS'
FUNCSTART, FUNCINITIALIZE, FUNCGUESS = 'func_start', 'func_initialize', 'func_guess'

        
#function pointers
#"State" is the name of the class

State = type("State", (object,), {})

class State:
    #Static
    movieguessed = False
    def __init__(self):
        print("In super Init")
        self.sm = "abbbbbbbbb"
        self.selectedmovie = None
        self.list_dashes = []
        
    #subroutine to make the list into a single string
    def convert_listtostring(self, list_dashes):
        dashes = ""
        dashes  = dashes.join(list_dashes)
        return dashes
    
class Guess(State):
    def __init__(self):
        print("Guess class init")
        self.state = GUESS
        super().__init__()
        
    #callback function
    def callbackfunc(self, list_dashes):
        if('_  ' not in list_dashes):
            return True
        else: return False
        #return(list_dashes)
    
    #subroutine to decide if the movie has been guessed
    def check_movieguessed(self, callbackfunc):
        if(callbackfunc(State.list_dashes)):
            State.movieguessed = True
        #else:
         #   self.movieguessed = False
        



    def Execute(self):
        print("Executing Guess State")
        print(State.selectedmovie)
        
        guessedletter = input("Guess a letter: ")
        #guessedletter = guessedletter
        print("Guessed letter = ", guessedletter)
        
        #find if the letter is there in the moviename
        #finds only the first letter
        #found_index = State.selectedmovie.find(guessedletter)
        #adds it in a list
        foundlist = [found_index.start() for found_index in re.finditer(guessedletter, State.selectedmovie)]

        #print("found index = ", found_index)
        #if(found_index != -1):
        if(len(foundlist) != 0):
            print("found the guessed letter")
            #replace the found letter into the list of dashes, convert it into a string and display
            #also check if game is over
            for found_index in foundlist:
                State.list_dashes[found_index] = guessedletter + '  '
                dashes = super().convert_listtostring(State.list_dashes)
                print(dashes)
            #if(self.check_movieguessed(State.list_dashes)):
            self.check_movieguessed(self.callbackfunc)
                #print("game over, you guessed all letters and won")
        else:
            #reduce guesses if letter not found
            #numberofguesses = numberofguesses - 1
            #print("Started hanging {} turns left".format(numberofguesses))
            self.movieguessed = False
        
class Start(State):
    def __init__(self):
        print("Start class init")
        self.state = START
        super().__init__()
    def Execute(self):
         print("Executing Start State")
         print(super().selectedmovie)
         print("Executing Start State Ends here")

class Initialize(State):
    def __init__(self):
        print("Initialize class init")
        self.state = INITIALIZE
        super().__init__()
    #maintain dashes as a list, since strings are immutable
    #subroutine to create as many dashes as the selected movie name and return a list
    def make_dashes(self):
        list_dashes = []
        for i in range(0, len(State.selectedmovie)):
            list_dashes.append("_  ")
        return list_dashes

    

    def Execute(self):
        print("Executing Initialize State")
        #TODO: handle spaces later
        #TODO: movie name is too long and you want to guess all at once without hanging
        movielist = [ 'gonewiththewind', 'diehard', 'soundofmusic', 'breakfastattiffany''s']
        #range of one less than the last item - 0 to 3
        movieitem =  random.randint(0, len(movielist)-1)
        #the movie selected
        #only this is maintained in the state object
        State.selectedmovie = movielist[movieitem]
        print("selected movie = ", State.selectedmovie)
        #User message
        print("Are you ready for a game of hangman?")


        #list of dashes
        State.list_dashes = self.make_dashes()
        #replace the vowels
        vowels = ['a', 'e', 'i', 'o', 'u']

    
        print("selected movie = ", State.selectedmovie)
        print("dashes string", State.list_dashes)

        #Nested loop to replace the vowels in the list of dashes
        for i in range(0, len(State.selectedmovie)):
            for vowel in vowels:
                if(vowel == State.selectedmovie[i]):
                    #put in a vowel and two spaces for beauty
                    State.list_dashes[i] = vowel + '  '
        print("new list of dashes = ", State.list_dashes)

        #convert list to string to display to the user
        dashes = super().convert_listtostring(State.list_dashes)
        print("Now guess this movie")
        print(dashes)
        State.sm = "abcdef"
        print(State.sm)
        print("Executing Initialize State Ends here")
        

        
class Transitioning:
    def __init__(self, toState):
        print("Transition object init")
        self.toState = toState

    def Execute(self):
        print("Executing Transitioning to {}".format(self.toState.state))

class FSM:

    #@staticmethod
    #def func_start():
    #    print("The game has started")

    def __init__(self, compplayer):
        self.compplayer = compplayer
        #The states are the strings
        #self.states = [START, INITIALIZE, GUESS]
        self.states = {}
        #Current and final state is start - set it to None instead
        self.currentstate = None
        #functions to call on a specific state, the map is maintained here
        #self.transitions = {FUNCSTART: Start, INITIALIZE:FUNCINITIALIZE, GUESS:FUNCGUESS}
        self.transitions = {}
        #current transition - Name of the Transition object with the state
        self.transitionto = None
        
        #calling th function associated with start
        #can't call a non-static function inside __init__
        #not a good idea - refactor

        #Move the place not here
        
        #self.statehandlers[FUNCSTART]()        

    def setState(self, statename):
        self.currentstate = statename
        

    def Transition(self, transto):
        self.transitionto = self.transitions[transto]
    
    def Execute(self):
        #If Transition to is not None
        if(self.transitionto):
            self.transitionto.Execute()
            self.setState(self.transitionto.toState)
            #Resetting it to None
            self.transitionto = None
        #Execute the current state
        self.currentstate.Execute()

class CompPlayer:
    def __init__(self):
        self.FSM = FSM(self)
        self.Start = 0

#constant to maintain max guesses
MAXGUESSES = 7

def main():
    #instantiating fsm object of the FSM class
    player = CompPlayer()

    #Intialize the state objects and store it in the states dictionary in FSM object
    player.FSM.states[START] = Start()
    player.FSM.states[INITIALIZE] = Initialize()
    player.FSM.states[GUESS] = Guess()

    player.FSM.transitions[FUNCSTART] = Transitioning(player.FSM.states[START])
    player.FSM.transitions[FUNCINITIALIZE] = Transitioning(player.FSM.states[INITIALIZE])
    player.FSM.transitions[FUNCGUESS] = Transitioning(player.FSM.states[GUESS])

    print("\n\nSetting state to start\n\n")
    player.FSM.setState(START)
    #one state wasted for start
    #TODO: move this for loop to guess state
    for numberofguesses in range(0, MAXGUESSES+ 1):
        print("In the guess loop")
        print(State.movieguessed)
        print(numberofguesses)
        if(not(State.movieguessed)):
            #Not yet guessed
            #The transition diagram implemented here
            #If the state is start

            #TODO: Change the boolean to transitioning object's to state
            if(player.Start == 0):
                player.FSM.Transition(FUNCINITIALIZE)
                player.Start = 1
            elif(player.Start == 1):

                #show vowels etc
                player.FSM.Transition(FUNCGUESS)
                player.Start = 2
                
            elif(player.Start == 2):
                #before transitioning how will I get some value from the instance of guessed? Have to store movieguessed in State
                # and that too static since the state are in the transition objects
                
                player.FSM.Transition(FUNCGUESS)
                player.Start = 2
                
            #Not yet guessed - execute method for all
            player.FSM.Execute()
        else:
            player.FSM.Transition(FUNCSTART)
            player.Start = 0
            print("You guessed it right! HOORAY!")
            break
    #came out of the loop not because of the break but because of the guesses being over
    if(State.movieguessed == False):
        print("Outside the for loop - all guesses over and not guessed")
    else:
        print("Guessed and took the right number of moves, HURRAY!")
if __name__ == "__main__":
    main()    




