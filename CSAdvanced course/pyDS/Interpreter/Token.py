
"""Token Types"""
#EOF has been added to identify end of the math expression
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LEFTPAREN', 'RIGHTPAREN', 'EOF'

"""Token class which denotes a token and its value"""
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

