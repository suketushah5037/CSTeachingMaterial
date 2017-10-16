import Lexer
import Token
from graphviz import Source
    
#Add it to a tree
class AST(object):
    pass
class BinOpNode(AST):
    def __init__(self, left, op, right):
        self.opvalue = op
        self.left = left
        self.right = right

class NumNode(AST):
    def __init__(self, token):
        self.token =  token
        #I do not have a token class as of now
        #self.value = self.token.value




#Parser proceeds through the tokens using the context free grammar and makes an AST

#bnf
#expr = expr op expr
#expr = number
#operator = +/-//or *
#number = 0-9
#expression = (expression)

#ebnf
"""
non terminals
lower precedence expanded first
 expr   : term ((PLUS | MINUS) term)*
 same precedence together
 term   : factor ((MUL | DIV) factor)*
 factor : INTEGER | LPAREN expr RPAREN

 terminals = 0-9 or later decimals?
"""

#parser = Parser("(111+2) *33-5 /45")

"""Parser class that evaluates a grammar and produces an AST. Recursive descent parser"""
#Picks up the tokens, builds a parse tree and put the tree on the stack
#each non terminal write a parse method and it gets only the tokens it needs and the tokens go on the stack
#Each parse methods will call other parse methods
#Each method  leaves one result on the stack
#| leads to if-else
class Parser(object):
    """constructor maintains the current token and the lexer """
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self.evalstack = []
        self.stack = []
    def error(self):
        raise Exception("not the right syntax")
    
    def consumetoken(self, token_type):
        if(self.current_token.type == token_type):
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
    """ factor : INTEGER | LPAREN expr RPAREN"""
    def factor(self):
        token = self.current_token
        print("in factor", token.value)
        if(token.type == Token.INTEGER):
            self.consumetoken(Token.INTEGER)
            print(token.value)
            #return(NumNode(token))
            return(BinOpNode(None, token.value, None))
        elif(token.type == Token.LPAREN):
            self.consumetoken(Token.LPAREN)
            node = self.expr()
            self.consumetoken(Token.RPAREN)
            return node
    """term   : factor ((MUL | DIV) factor)* """
    def term(self):
        node = self.factor()

        while(self.current_token.type in (Token.MUL, Token.DIV)):
            token = self.current_token
            print("in term", token.value)
            #consume shoudl consume the correct token passed, hence we differentiate
            #between a PLUS and a MINUS
            if(token.type == Token.MUL):
                self.consumetoken(Token.MUL)
            elif(token.type == Token.DIV):
                self.consumetoken(Token.DIV)
            rightnode = self.factor()
            node = BinOpNode(node, token.value, rightnode)
        return node
    
    """expr   : term ((PLUS | MINUS) term)* """
    def expr(self):
        node = self.term()

        while(self.current_token.type in (Token.PLUS, Token.MINUS)):
            token = self.current_token
            print("in expr", token.value)
            #consume shoudl consume the correct token passed, hence we differentiate
            #between a PLUS and a MINUS
            if(token.type == Token.PLUS):
                self.consumetoken(Token.PLUS)
            elif(token.type == Token.MINUS):
                self.consumetoken(Token.MINUS)
            node = BinOpNode(node, token.value, self.term())
        return node
    #recursion and use a stack
    #My construction does not use a stack- why here then???
    def evaluatemathExprTree(self, tree):
        #Bug
        #stack = []
        #Recursion - stack is being emptied every time

        #make it global it is recursive
        #value = 0
        if tree is not None:
            self.evaluatemathExprTree(tree.left)
            self.evaluatemathExprTree(tree.right)
            #print(tree.opvalue)
            if(tree.opvalue == '+'):
                op1 = self.evalstack.pop()
                op2 = self.evalstack.pop()
                #print("op1 = ", op1)
                #print("op2 = ", op2)
                self.evalstack.append(float(op1) + float(op2))
                self.printstack()
            elif(tree.opvalue == '-'):
                #print(tree.opvalue)
                #print(stack.pop())
                op1 = self.evalstack.pop()
                op2 = self.evalstack.pop()
                #print(int(op1))
                #print(int(op2))
                #Bug: int typecasting uses 0.8 as 0
                self.evalstack.append(float(op1) - float(op2))
                self.printstack()
            elif(tree.opvalue == '*'):
                op1 = self.evalstack.pop()
                op2 = self.evalstack.pop()
                self.evalstack.append(float(op1) * float(op2))
                self.printstack()
            elif(tree.opvalue == '/'):
                op1 = self.evalstack.pop()
                op2 = self.evalstack.pop()
                #popped one is the last operator :BUG
                self.evalstack.append(float(op2) / float(op1))
                self.printstack()
            else:
                self.evalstack.append(float(tree.opvalue))
                self.printstack()
            return(self.evalstack[-1])

    def printstack(self):
        i = len(self.evalstack)-1
        stackstr = ""
        while(i >= 0):
            stackstr = stackstr + " ||" + str(self.evalstack[i])
            i=i-1
        print(stackstr)
    
    
#Inorder traversal
def inorder(tree):
    if tree is not None:
        inorder(tree.left)
        print(tree.opvalue)
        inorder(tree.right)



import textwrap

dot_header = [textwrap.dedent("""\
        digraph astgraph {
          node [shape=circle, fontsize=12, fontname="Courier", height=.1];
          ranksep=.3;
          edge [arrowsize=.5]
        """)]

""" inorder traversal"""
def visitast(tree):
    global ncount
    global dot_body
     
    #numeric and leaf node
    if((tree.left == None) and (tree.right == None)):
        s = '  node{} [label="{}"]\n'.format(ncount, tree.opvalue)
        dot_body.append(s)
        tree._num = ncount
        ncount += 1
        print(tree.opvalue)
        return
        #visitast(tree)
    #binop node
    elif(tree.opvalue == Token.EOF):
         return
    else:
        s = '  node{} [label="{}"]\n'.format(ncount, tree.opvalue)
        print(tree.opvalue)
        dot_body.append(s)
        tree._num = ncount
        ncount = ncount+ 1
        visitast(tree.left)
        visitast(tree.right)

        for child_node in (tree.left, tree.right):
            s = '  node{} -> node{}\n'.format(tree._num, child_node._num)
            dot_body.append(s)

#pip install graphviz on the command prompt
#generating ast graph

ncount = 1
dot_body = []
dot_footer = ['}']

def gendot(tree):
    global ncount
    global dot_body
    global dot_header
    global dot_footer
    visitast(tree)
    return ''.join(dot_header + dot_body  + dot_footer)



#bfs tree uses a queue and dfs uses a stack




        
lexer = Lexer.Lexer("1*(2+3)/2")       
myparser = Parser(lexer)

node = myparser.expr()
value = myparser.evaluatemathExprTree(node)

print("calculated value = ", value) 
if(node == None):
    print("parse returned none")
else:
    print(node)
print("Inorder traversal")
inorder(node)
#print(myparser.evaluatemathExprTree(node))

###################################################
print("printing ast tree")
content = gendot(node)
print(content)



print("printing abstract syntax tree")
nodecount = 1
dot_body = []
dot_footer = ['}']

def gendotbfs(tree):
    global dot_header
    global dot_body
    global dot_footer
    bfs(tree)
    return(''.join(dot_header + dot_body + dot_footer))
def bfs(tree):
    global ncount
    global dot_body
    ncount = 1
    queue = []
    queue.append(tree)
    s = '  node{} [label="{}"]\n'.format(ncount, tree.opvalue)
    dot_body.append(s)
    tree._num = ncount
    ncount += 1

    while queue:
        tree = queue.pop(0)
        #print("tree opvalue", tree.opvalue)
        for child_node in (tree.left, tree.right):
             if(child_node  == None):
                 #numeric node 
                 continue
             #print("ncount and child node = ", ncount, child_node.opvalue)
             s = '  node{} [label="{}"]\n'.format(ncount, child_node.opvalue)
             #print(s)
             dot_body.append(s)
             child_node._num = ncount
             ncount = ncount + 1
             #print("node{} -> node{} ".format( tree._num,child_node._num))
             s = '  node{} -> node{}\n'.format(tree._num,child_node._num)
             #print(s)
             dot_body.append(s)
             queue.append(child_node)


print("tree root node", node)
content = gendotbfs(node)
print(content)

#install graphviz from here
#download from http://www.graphviz.org/Download_windows.php and install
#run http://www.graphviz.org/Download_windows.php

#command to run
#C:\Program Files (x86)\Graphviz2.38\bin>dot -Tpng -o "C:\Users\Gowri\Desktop\CS_classes\MaterialRepo\CSTeachingMaterial\CSAdvanced course\pyDS\tokenizer\parsetree.png" "C:\Users\Gowri\Desktop\CS_classes\MaterialRepo\CSTeachingMaterial\CSAdvanced course\pyDS\tokenizer\parsetree.dot"

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
