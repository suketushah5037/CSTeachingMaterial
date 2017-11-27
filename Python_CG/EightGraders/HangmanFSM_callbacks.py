#Outside the library
#This is the hangman player who knows how many states are there and the state transitions

from functools import partial

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
        self.FSM = FSM(model=self, states=CompPlayer.states, initial=START)
        self.name = name
        #Any other hangman player can choose a different number of guesses for hiimself
        self.numberofguesses = MAXGUESSES
        
        #add transitions
        #Triggers are the strings on which player object is expected to 
        #change transitions
        self.FSM.add_transition(trigger=TRSTART, source=START, dest=INITIALIZE)
        self.FSM.add_transition(trigger=TRINITIALIZE, source=INITIALIZE, dest=GUESS)
        self.FSM.add_transition(trigger=TRGUESS, source=GUESS, dest=GUESS)
        #TODO: later change to, do you want to play again and restart
        self.FSM.add_transition(trigger=TREND, source=GUESS, dest=END)
        

#################################
##Filling stubs now
#Step1:Now need an FSM class to store transitions and transitions store states
#A private indicated function to get the trigger name-helper func
def _get_trigger(model, trigger_name, *args, **kwargs):
    """Convenience function added to the model to trigger events by name.

    Args:
        model (object): Model with assigned event trigger.
        trigger_name (str): Name of the trigger to be called.
        *args: Variable length argument list which is passed to the triggered event.
        **kwargs: Arbitrary keyword arguments which is passed to the triggered event.
    Returns:
        bool: True if a transitions has been conducted or the trigger event has been queued.
    """
    func = getattr(model, trigger_name, None)
    if func:
        return func(*args, **kwargs)
    
class FSM:
    #hardcoding self  - does it mean compplayer since FSM object is created by compplayer
    #all triggering events will be attached to FSM
    def __init__(self, model='self', states=None, initial=START):
        #add states
        self.states = dict()
        self.add_states(states)


        #set the initial state
        self.initial = initial


        #add transitions
        #added transitions from the player itself

        
        #add the model or FSM to the player. The transition triggers are
        #attached to the model
        #model is the player object
        #We have only one model as a simplification
        self.add_model(model)


    def add_states(self, states):
        print("adding states")
        pass

    def add_transition(self, trigger, source, dest):
        #Step3:need to fill this in now
        print("adding transition")
        pass

    #when initial is not passed it is None
    def add_model(self, mod, initial=None):
        #Step2: fill in
        #initialize triggers and callbacks

        #adding a instace variable to player dynamically  and using
        #partial to call "_get_triggger" without any knowledge of the trigger name
        #the trigger is trstart for example
        #"_get_trigger" should call trstart and assign the return value in mod.trigger
        mod.trigger = partial(_get_trigger, mod)
        

################################

def main():
    #hangmanplayer is the name of the player
    player = CompPlayer("HangmanPlayer")
    #Notice the name of the trigger is a function name on the player object
    player.trstart()


if __name__ == "__main__":
    main()
    





        
