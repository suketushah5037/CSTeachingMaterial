"""Not using this as of now. This is to represent an integer node and it has the token"""
class NumNode(AST):
    def __init__(self, token):
        self.token =  token
        #I do not have a token class as of now
        #self.value = self.token.value

##############################################################################
#OLD CODE
##class Parser(object):
##    def printstack(self):
##        i = len(self.evalstack)-1
##        stackstr = ""
##        while(i >= 0):
##            stackstr = stackstr + " ||" + str(self.evalstack[i])
##            i=i-1
##        print(stackstr)
##    
##    #recursion and use a stack
##    def evaluatemathExprTree(self, tree):
##        #Bug
##        #stack = []
##        #Recursion - stack is being emptied every time
##
##        #make it global it is recursive
##        #value = 0
##        if tree is not None:
##            self.evaluatemathExprTree(tree.left)
##            self.evaluatemathExprTree(tree.right)
##            print(tree.opvalue)
##            if(tree.opvalue == '+'):
##                op1 = stack.pop()
##                op2 = stack.pop()
##                self.evalstack.append(float(op1) + float(op2))
##                self.printstack()
##            elif(tree.opvalue == '-'):
##                #print(tree.opvalue)
##                #print(stack.pop())
##                op1 = stack.pop()
##                op2 = stack.pop()
##                #print(int(op1))
##                #print(int(op2))
##                #Bug: int typecasting uses 0.8 as 0
##                self.evalstack.append(float(op1) - float(op2))
##                self.printstack()
##            elif(tree.opvalue == '*'):
##                op1 = stack.pop()
##                op2 = stack.pop()
##                self.evalstack.append(float(op1) * float(op2))
##                self.printstack()
##            elif(tree.opvalue == '/'):
##                op1 = stack.pop()
##                op2 = stack.pop()
##                self.evalstack.append(float(op1) / float(op2))
##                self.printstack()
##            else:
##                self.evalstack.append(float(tree.opvalue))
##                self.printstack()
##    """Maitains the lexer and the math expression"""
##    def __init__(self, mathexpr):
##        self.mathexpr = mathexpr
##        self.lexer = Lexer.Lexer(mathexpr)
##        self.current_token = None
##        self.ast = None
##        self.stack = []
##        self.evalstack = []
##
##    
##    def factor(self):
##        node = self.ast
##        #get the current token
##        self.current_token = self.lexer.get_next_token()
##
##        if(self.current_token.type == Lexer.Token.INTEGER):
##            #not using numnode for now
##            #node = NumNode(self.current_token)
##            node = BinOpNode(None,self.current_token.value,None)
##            #consume it and and add operator in the stack
##            #added the operator on the stack
##            self.stack.append(node)
##            #BUG:consumedont consume here, happening at the term function
##            self.current_token = self.lexer.get_next_token()
##            #Debugging
##            print("factor int token type = ", self.current_token.type)
##            print("factor int token value = ", self.current_token.value)
##            
##            #Debugging
##            print("factor int node value = ", node.opvalue)
##            print("factor int node left = ", node.left)
##            print("factor int node right = ", node.right)
##            return node
##        elif(self.current_token.type == Lexer.Token.LPAREN):
##            #consume it and and add operator in the stack
##            #consume
##            self.current_token = self.lexer.get_next_token()
##            node = expression()
##            #Debugging
##            print("factor paren value = ", node.opvalue)
##            print("factor paren left = ", node.left)
##            print("factor paren right = ", node.right)
##            return node
##        elif(self.current_token.type == Lexer.Token.RPAREN):
##            print("right paren")
##            self.current_token = self.lexer.get_next_token()
##            return self.ast #????
##        elif(self.current_token.type == Lexer.Token.EOF):
##            print("EOF")
##            
##            node = BinOpNode(None,self.current_token.value,None)
##            #Debugging
##            print("factor eof value = ", node.opvalue)
##            print("factor eof left = ", node.left)
##            print("factor eof right = ", node.right)
##            return node
##            
##    """term   : factor ((MUL | DIV) factor)* """
##    def term(self):
##        node = self.ast
##        node = self.factor()
##        newnode = BinOpNode(None, None, None)
##        #BUG: not required here - happening inside the while get the current token
##        #self.current_token = self.lexer.get_next_token()
##        #Debugging
##        print("term token type = ", self.current_token.type)
##        print("term token value = ", self.current_token.value)
##        
##        while(self.current_token.type in (Lexer.Token.MUL, Lexer.Token.DIV)):
##            #consume it and and add operator in the stack
##            #added the operator on the stack
##            self.stack.append(node)
##            #consume
##            self.current_token = self.lexer.get_next_token()
##            #Debug
##            print("term post consume token type = ", self.current_token.type)
##            print("term post consume token value = ", self.current_token.value)
##            #Calling to get the next term
##            newnode = self.factor()
##            if(self.current_token.type == Lexer.Token.MUL):
##                self.ast = BinOpNode(node,'*',newnode)
##            elif(self.current_token.type == Lexer.Token.DIV):
##                self.ast = BinOpNode(node,'/',newnode)
##
##
##        #Debugging
##        print("term node value = ", node.opvalue)
##        print("term node left = ", node.left)
##        print("term node right = ", node.right)
##
##        print("term newnode value = ", newnode.opvalue)
##        print("term newnode left = ", newnode.left)
##        print("term newnode right = ", newnode.right)
##        
##        return node
##          
##    """expr   : term ((PLUS | MINUS) term)* Parses the expression - the upper most"""
##    def expression(self):
##        node = self.ast
##        #calling to get the first term
##        node = self.term()
##        newnode = BinOpNode(None,None,None)
##        #BUG: dont consume here . happening in while get the current token
##        #self.current_token = self.lexer.get_next_token()
##        #Debugging
##        print("expr token type = ", self.current_token.type)
##        print("expr token value = ", self.current_token.value)
##        
##        while(self.current_token.type in (Lexer.Token.PLUS, Lexer.Token.MINUS)):
##            #consume it and and add operator in the stack
##            #added the operator on the stack
##            self.stack.append(node)
##            #consume
##            self.current_token = self.lexer.get_next_token()
##            #Debug
##            print("expr post consume token type = ", self.current_token.type)
##            print("expr post consume token value = ", self.current_token.value)
##            #Calling to get the next term
##            newnode = self.term()
##            if(self.current_token.type == Lexer.Token.PLUS):
##                self.ast = BinOpNode(node,'+',newnode)
##            elif(self.current_token.type == Lexer.Token.MINUS):
##                self.ast = BinOpNode(node,'-',newnode)
##        #Debugging
##        print("expr node value = ", node.opvalue)
##        print("expr node left = ", node.left)
##        print("expr node right = ", node.right)
##
##        print("expr newnode value = ", newnode.opvalue)
##        print("expr newnode left = ", newnode.left)
##        print("expr newnode right = ", newnode.right)
##        
##        return node
##
##    def parse(self):
##        node = self.expression()
##
##        #Debugging
##        print("parse value = ", node.opvalue)
##        print("parse left = ", node.left)
##        print("parse right = ", node.right)
##        return node
