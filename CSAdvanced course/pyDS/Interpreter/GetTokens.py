#To get tokens
import Lexer

#If not loaded from a module, the __name__ variable is set to "__main__", else
#it is set to the module's name

#this if condition is written when you dont want this parantheses check code to run
#when imported as a module but only when it is the main driver
if __name__ == "__main__":
    #This is my sample math expression
    mathexpr = "(111+2) *33-5 /45"

    tokenizer = Lexer.Lexer(mathexpr)

    token = tokenizer.get_next_token()
    while(token.type != Lexer.Token.EOF):
        print(token.type, token.value)
        token = tokenizer.get_next_token()
