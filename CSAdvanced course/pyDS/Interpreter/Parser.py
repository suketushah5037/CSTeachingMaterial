#To advance tokens
import Lexer
#To identify tokens
import Token

#Not required now, since the code is only producing the text for the dot file, and the dot file is fed on the command prompt to graphviz tool to produce the abstract syntax tree
#from graphviz import Source
    
#Add it to a tree
"""Abstraction of a syntax  tree, the mathematical expression is fed to the lexer to produce tokens and the
tokens are stored in a tree, whose each node is a BinOp node or integer node or a bracket. For simplicity,
assume we have BinOp and Integer alone and Integer is a BinOp node that does not have left and Right children"""
class AST():
    pass

""" All children are BinOp nodes, Integers are also BinOp nodes with left and right children as None. The opvalue should ideally be a token, with the type and value.
Inherits from Abstract syntax tree. This is required when we attach NumNode and want to denote that every node irrespective of the type is a form of AST node"""
class BinOpNode(AST):
    def __init__(self, left, op, right):
        self.opvalue = op
        self.left = left
        self.right = right




#Parser proceeds through the tokens using the context free grammar and makes an AST

#bnf Backus-Naur Form
#expr = expr op expr
#expr = number
#operator = +/-//or *
#number = 0-9
#expression = (expression)
#ebnf
"""
FSM and RPN introduced first. TODO: List RPN ambiguity example here.

This is called a recursive descent parser. It is the easiest. There are algorithms for other kinds of parsers too.

All mathematical expressions, follow a pattern, and to indentify the pattern and directly translate them to code, there is a grammmar like the English grammar.
A state machine diagram is drawn and converted to a grammar in the EBNF form.

Then it is translated to code verbatim where each line is a function. The code in the function is word by word translation of the EBNF form.
The * means there is a while loop. Each method leaves, token(s) on the stack

Parser proceeds through the tokens using the context free grammar and makes an AST. Finally when the node is returned it returns the root node of the abstract syntax tree

AST is the mathematical expression written in RPN (1+2+3 is written as 12+3+, here there is no ambiguity in on which operator needs to be applied on first.
The precedence is not in the mind but in the expression. And this form is constructed into a tree.

Technicalities :
Tree, Stack and Queue used here.
Traversal techniques are BFS and DFS
BFS uses a queue
DFS uses a stack - DFS has three types, preorder, inorder and postorder traversals

EBNF - Extended backus naur form
non terminals
lower precedence expanded first
 expr   : term ((PLUS | MINUS) term)*
 same precedence together
 term   : factor ((MUL | DIV) factor)*
 factor : INTEGER | LPAREN expr RPAREN

 terminals = 0-9 or later decimals?
"""

#parser = Parser("(111+2) *33-5 /45")

"""Parser class that evaluates a grammar and produces an AST. Recursive descent parser
The tree is maintained by providing the left and right nodes for a particular node, the final node returned is the
root of the tree"""
#Picks up the tokens, builds a parse tree and put the tree on the stack
#each non terminal write a parse method and it gets only the tokens it needs and the tokens go on the stack
#Each parse methods will call other parse methods
#Each method  leaves one result on the stack
#| leads to if-else
class Parser():
    """constructor maintains the current token and the lexer and the expression evaluation stack only to evaluate expressions"""
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
                
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
            #consume should consume the correct token passed, hence we differentiate
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


    
    
#Inorder traversal
def inorder(tree):
    if tree is not None:
        inorder(tree.left)
        print(tree.opvalue)
        inorder(tree.right)






















#print("Inorder traversal")
#inorder(node)






#print("printing abstract syntax tree")
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


#print("tree root node", node)
#content = gendotbfs(node)
#print(content)

