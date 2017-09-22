#FSM for math expressions - to check the grammar
#Convert to infix to  disallow precendence

#Play FSM game first and then evaluate FSM for math expressions and
#convert it into pseudo code/code
#calculate - evaluate on the fly

#Do not consider unary operators or decimals
#Check if balanced or not initially
mathexpr = ((55)+3)*300/44+(6*9)-714/453

#?assume it is balanced for now
#Loop through all the characters in the mathexpr

#First tokenize them
#Called lexical analysis or lexer

#See the problem, I am facing, if I do not tokenize? I need to use multiple
#
##for char in mathexpr:
##    #assuming we have only binary operators, 
##    firstnumber = ""
##    secondnumber = ""
##    if(char == '('):
##        #Move on to the next character
##        #Push on to the stack
##    if(char == ')'):
##        #Move on to the next character
##        #evaluate and pop the whole expression till the opening brace from the stack
##    if(isdigit(char)):

"""
Lexical analyser - split the mathematical expression into tokens and provide tokens
Assuming no whitespaces
"""
class Lexer:
    """
    Constructor - stores the math expression, the position and current char
    """
    def __init__(self, text):
        self.mathexpr = text
        #position of the index in the expression
        self.pos = 0
        self.current_char = self.mathexpr[self.pos]
    """
    An error if an invalid character is provided
    """
    def error(self):
        raise Exception("Invalid character")
    """
    Collects all the digits and returns the integer token
    """
    def integer(self):
        collectinteger = ''
        while(self.current_char is not None):
            collectinteger = collectinteger + self.currentchar
            self.advance()
        #If None it comes here
        return int(collectinteger)
    def advance(self):
    def get_next_token(self):
        
