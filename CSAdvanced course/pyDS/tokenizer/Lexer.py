#This is my sample math expression
#mathexpr = "(111+2) *33-5 /45"

#Identify tokens - importing from Token class
import Token

#tokens are paranthesis operators and operands
#Lexer splits an expression to tokens

#Introducing: Exception are to identify possible errors in the program and throw up the right
#messages
"""
Returns Tokens and Advances tokens based on the input. Manages integers and whitespaces
"""
#Exercise: unary operator and exponentiation
class Lexer(object):
    """Maintains the current position and current character in the math expression"""
    def __init__(self, mathexpr):
        self.mathexpr = mathexpr
        #Initially position is 0 is the array
        self.pos = 0
        self.current_char = self.mathexpr[self.pos]
    """Raises invalid character exception"""
    def error(self):
        raise Exception('Invalid character')
    """Advance one position - mind you not the next token """
    def advance(self):
        #Reset the state of the object
        #If it reaches the end - the current character is none
        self.pos += 1
        if(self.pos > (len(self.mathexpr) - 1)):
            self.current_char = None
        else:
            self.current_char = self.mathexpr[self.pos]
    
    """Skip white spaces - advance position if not the end or if it is a white space"""
    def skip_whitespace(self):
        #Could use regex here and trim white spaces
        #just iterate and advance the current position when there is a white space
        #Using char.isspace() given by python
        while(self.current_char is not None and self.current_char.isspace()):
            self.advance()

    """Identifies integer token - 555/55/5 all are integers """
    #Exercise: How to you handle floating point tokens
    def integer(self):
        #Use isdigit to identify an integer
        #Logic is that when it is a digit all other digits as part of the sae number are contiguous
        num_from_digits_string = ''
        while(self.current_char is not None and self.current_char.isdigit()):
            num_from_digits_string += self.current_char
            self.advance()
        #Should be float here - in case of a decimal token
        return int(num_from_digits_string)
    
    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while (self.current_char is not None):

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token.Token(Token.INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token.Token(Token.PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token.Token(Token.MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token.Token(Token.MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token.Token(Token.DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token.Token(Token.LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token.Token(Token.RPAREN, ')')

            self.error()

        return Token.Token(Token.EOF, None)
