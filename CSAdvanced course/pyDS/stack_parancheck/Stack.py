#Use cases of stacks
#Anagram detection and Parentheses checks

#Class data structure to store items in a stack
#The list (implemented as an array beneath) is morphed into a stack

#?check how array expansion happens when limit gets over

#?Explain self

#Doc strings - strings that help in documentation

#?PDB - for debugging

"""
The Stack Data Structure defined
Stacks are LIFO structures, LIFO, the last one that goes in comes out first
Just like the plates in a stack or a deck of cards
Why an extra class? Just as an abstraction to provide only functionalites relevant
to a a stack, you cannot remove from or insert in between
"""
class Stack:
    #Constructor
    #All variables declard here are class variables
    """
    Stack's constructor, holds and initializes the "items" list
    """
    def __init__(self):
        #All varibales declared here are member variables

        #Define the list data structure which is going to behave as a Stack
        #Define an empty list
        self.items = []

    """
    Pushes an item on to the stack
    """
    def push(self, item):
        #push item using append
        self.items.append(item)

    """
    Pops an item from the stack
    """
    def pop(self):
        #pop the top most item - removes it as well
        return self.items.pop()

    """
    See what is the top most item
    Does not remove the item
    """
    def peek(self):
        return self.items[len(self.items) - 1]

    """
    The number of items in the stack
    """
    def size(self):
        return len(self.items)

    
