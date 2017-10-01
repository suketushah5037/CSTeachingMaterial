#Where are stacks queues and trees used?


mathexpr = "1+2*3-5/4"


#Convert it into postfix
mathexpr = "123*+54/-"

#Tokens
INTEGER, MUL,DIV, ADD, SUB, EOF = 'INTEGER', 'MUL', 'DIV', 'PLUS', 'MINUS', 'EOF'

#Add it to a tree
class AST(object):
    pass
    

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
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

#Have the lexer create tokens and give out tokens
#Have the parser create an expression tree

#assume it is postfix
#tokenize and AST at the same place

def constructTree(mathexpr):
    stack = []
    for char in mathexpr:
        if( (char == '+') or (char == '-') or (char == '*') or (char == '/') ):
            operand2 = stack.pop()
            operand1 = stack.pop()
            opNode = BinOpNode(operand1,char,operand2)
            #Append the tree to the stack
            #print(opNode)
            stack.append(opNode)
        else:
            #Operand - numeric
            numNode = BinOpNode(None,char, None)
            print(numNode)
            stack.append(numNode)
    #Returns the top most in the expresion tree - the '-' node with the whole tree in
    #the above math expresssion
    #print(stack[-1].left)
    return stack[-1]       

#Inorder traversal
def inorder(tree):
    if tree is not None:
        inorder(tree.left)
        print(tree.opvalue)
        inorder(tree.right)
        

#Preorder traversal
def preorder(tree):
    if tree is not None:
        print(tree.opvalue)
        preorder(tree.left)
        preorder(tree.right)



#Postorder traversal
def postorder(tree):
    if tree is not None:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.opvalue)
        
#Evaluate expression
#a postfix one
def evaluateMathExpr(mathexpr):
    value = 0
    stack = []
    for char in mathexpr:
        if(char == '+'):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(float(op1) + float(op2))
            printstack(stack)
        elif(char == '-'):
            op1 = stack.pop()
            op2 = stack.pop()
            #print(int(op1))
            #print(int(op2))
            #Bug: int typecasting uses 0.8 as 0
            stack.append(float(op1) - float(op2))
            printstack(stack)
        elif(char == '*'):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(float(op1) * float(op2))
            printstack(stack)
        elif(char == '/'):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(float(op1) / float(op2))
            printstack(stack)
        else:
            stack.append(float(char))
            printstack(stack)
    #the stack only has the value
    value = stack.pop()
    return value

def printstack(stack):
    i = len(stack)-1
    stackstr = ""
    while(i >= 0):
        stackstr = stackstr + " ||" + str(stack[i])
        i=i-1
    print(stackstr)

#recursion and use a stack
def evaluatemathExprTree(tree):
    #Bug
    #stack = []
    #Recursion - stack is being emptied every time

    #make it global it is recursive
    #value = 0
    if tree is not None:
        evaluatemathExprTree(tree.left)
        evaluatemathExprTree(tree.right)
        print(tree.opvalue)
        if(tree.opvalue == '+'):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(float(op1) + float(op2))
            printstack(stack)
        elif(tree.opvalue == '-'):
            #print(tree.opvalue)
            #print(stack.pop())
            op1 = stack.pop()
            op2 = stack.pop()
            #print(int(op1))
            #print(int(op2))
            #Bug: int typecasting uses 0.8 as 0
            stack.append(float(op1) - float(op2))
            printstack(stack)
        elif(tree.opvalue == '*'):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(float(op1) * float(op2))
            printstack(stack)
        elif(tree.opvalue == '/'):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(float(op1) / float(op2))
            printstack(stack)
        else:
            stack.append(float(tree.opvalue))
            printstack(stack)
    
            
value = 0        
tree = constructTree(mathexpr)
print("Tree constructed")
print("Evaluating with tree")
stack = []
evaluatemathExprTree(tree)
value = stack.pop()
print("Evaluated value with tree is = ", value)

#value = evaluateMathExpr(mathexpr)
#print("Evaluated value is = ", value)


#print(tree)
#print(tree.left)
#print(tree.right)

#AST given inorder-pre and post order
##print("Inorder tree")
##inorder(tree)
##print("Preorder tree")
##preorder(tree)
##print("Postorder tree")
##postorder(tree)

#parser - froming tokens


#output
#mathexpr = "123*+54/-"

#Without knowing precedence and associativity can't do itat all

##Create an empty stack called opstack for keeping operators. Create an empty list for output.
##Convert the input infix string to a list by using the string method split.
##Scan the token list from left to right.
##If the token is an operand, append it to the end of the output list.
##If the token is a left parenthesis, push it on the opstack.
##If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
##If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
##When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.

#process tokens, consider only single digit numbers as tokens
#left and right paranthesis - change precedence
#Need a stack and a queue
#Input is infix

def infixtopostfix():
    print("Converting infix to postfix")
    opstack = []
    evalqueue = []
    #infix to postfix - since usually expressions are infix
    mathexpr = "1+2*3-5/4"
    #use regex to split into tokens?
    #check balanced paranthesis and proper syntax using stack and regex

    #changing infix to postfix
    for char in mathexpr:
        if( (char == '+') or (char == '-') or (char == '*') or (char == '/') ):
            i = len(opstack)-1
            while(i >= 0):
                #implement precendence - for now if + or - * or / can be there in the opstack
                if( (char == '+') or (char == '-') ):
                    if( (opstack[i] == '*') or (opstack[i] == '/') ):
                        opchar = opstack.pop()
                        evalqueue.append(opchar)
                i = i -1
            #any operands having higher precendence append them to the evalqueue
            #push it finally
            opstack.append(char)
        elif(char == '('):
            opstack.append('(')
        elif(char == ')'):
            while(opstack[-1] != '('):
                operator = opstack.pop()
                evalqueue.append(operator)
        else:
            #change it to token later
            evalqueue.append(char)

    oper = opstack.pop()
    while(len(opstack) != 0):
        evalqueue.append(oper)
        oper = opstack.pop()
        
    print("printing from infix to postfix")
    print(evalqueue)

infixtopostfix()
#Convert it into postfix
mathexpr = "123*+54/-"

evaluateMathExpr(mathexpr)
