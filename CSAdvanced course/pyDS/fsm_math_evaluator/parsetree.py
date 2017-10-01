
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

#Advanced Exercise: Allow unary operators

#TODO: divide them into classes and only the parts the students' will work on

"""
Token class - to denote each token
The lexer's get next token returns a token
"""
INTEGER, MUL,DIV, ADD, SUB, EOF = 'INTEGER', 'MUL', 'DIV', 'PLUS', 'MINUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
##    def __str__(self):
##        #String representation of the class instance
##        return 'Token({type},{value})'.format(type=self.type, value=repr(self.value))
##    def __repr__(self):
##        return self.__str__()

        
"""
Lexical analyser - split the mathematical expression into tokens and provide tokens
Assuming no whitespaces

Exercise: Change this to allow whitespaces
"""
class Lexer:
    """
    Constructor - stores the math expression, the position and current char
    Assumes no whitespaces available
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
        #How will you know that you have not reached the end?You set current character
        #as None in advance
        while(self.current_char is not None and self.current_char.isdigit()):
            collectinteger = collectinteger + self.current_char
            self.advance()
        #If None it comes here
        return int(collectinteger)
    """
    Advances a character in the math expression
    """
    def advance(self):
        self.pos = self.pos + 1
        if(self.pos > len(self.mathexpr) - 1):
           self.current_char = None
        else:
           self.current_char = self.mathexpr[self.pos]
    """
    Creates Token objects of INTEGER, EOF, ADD, SUB, MUL, DIV types and returns
    the same and advances the po
    """
    def get_next_token(self):
        while self.current_char is not None:
            if(self.current_char.isdigit()):
                #The self.integer() advances as many tokens as continuous digits, like 555 or 55
                return(Token(INTEGER, self.integer()))
                #Return the intger as of now since my token class is not ready
                #return(self.integer())
            if(self.current_char == '*'):
                self.advance()
                return(Token(MUL, '*'))
            if(self.current_char == '/'):
                self.advance()
                return(Token(DIV, '/'))
            if(self.current_char == '+'):
                self.advance()
                return(Token(ADD, '+'))
            if(self.current_char == '-'):
                self.advance()
                return(Token(SUB, '-'))
            self.error()
        return(Token(EOF, None))

"""Empty AST"""        
class AST(object):
    pass

"""Represents a Number, inherting from AST"""
class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = self.token.value


"""BinOP node: Represents a binary operation, with a left and right node"""
class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

        
"""Parser - Takes tokens and generates AST"""
class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    """
    Error condition
    """
    def error(self):
        raise Exception('Invalid syntax')

    """Eat up the current token and move to the next"""
    def eat(self, token_type):
        if(self.current_token.type == token_type):
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """ factor: INTEGER | LPAREN expr RPAREN"""
        token = self.current_token
        if(token.type == INTEGER):
            self.eat(INTEGER)
            return Num(token)
        elif(token.type == LPAREN):
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

    def term(self):
        """ term: factor((MUL|DIV) factor)* """
        node = self.factor()
        while(self.current_token.type in (MUL,DIV)):
            token = self.current_token
            if(token.type == MUL):
                self.eat(MUL)
            elif(token.type == DIV):
                self.eat(DIV)
            node = BinOp(left = node, op=token, right = self.factor())
        return node

    def expr(self):
        """ expr: term ((PLUS|MINUS)term)*"""
        node = self.term()

        while(self.current_token.type in (ADD, SUB)):
              token = self.current_token
              if(token.type == ADD):
                  self.eat(ADD)
              elif(token.type == SUB):
                  self.eat(SUB)
              node = BinOp(left = node, op=token,right=self.term())
        return node
    def parse(self):
         return self.expr()


class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))
    
"""
Evaluates the expression, traverses through the parse tree and evaluates the expression
"""
class Interpreter(NodeVisitor):
    """
    Constructor - holds the lexer and the current Token (not the current position in the
    expression, like the Lexer). This is an abstraction over the Lexer
    """
    def __init__(self, parser):
        self.parser = parser

    """
    Error condition
    """
    def error(self):
        raise Exception('Invalid syntax')

    def visit_BinOp(self, node):
              if(node.op.type == ADD):
                  return self.visit(node.left)+self.visit(node.right)
              elif(node.op.type == SUB):
                  return self.visit(node.left)-self.visit(node.right)
              elif(node.op.type == MUL):
                  return self.visit(node.left)*self.visit(node.right)
              elif(node.op.type == DIV):
                  return self.visit(node.left)/self.visit(node.right)
    def visit_Num(self, node):
              return node.value

    def interpret(self):
              tree=self.parser.parse()
              return self.visit(tree)

"""
Main driver
Exercise: write the main driver
"""
#Indentation was below the class, it gave me an error
def main():
    #Infinite loop for the prompt to show up
    #Exercise fill this up
    while(True):
        try:
            text = input('calc> ')
        except EOFError:
            break
        #Nothing entered, check this with pdb
        if not text:
            continue
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)

if(__name__ == '__main__'):
    main()
             
