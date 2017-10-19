"""evaluates the mathematical expression from the tree root node received from the parser.
     Token     AST
Lexer--->Parser--->Interpreter
The prints - show the recursive calls and how the eval stack is maintained and the callstack status when the eval stack is manipulated
Notice how the call stack reduces when the 2+3 is evaluated and the 1*5 is evaluated and the 5/2 is evaluated
"""
import parser
import traceback

class Interpreter:
    def __init__(self, parser):
        self.parser = parser
        self.evalstack = []
    def interpret(self):
        print("--------------------------Building the AST-------------------------------")
        tree = self.parser.expr()
        print("--------------------------Building the AST-------------------------------")
        print("\n\n\n\n\n")
        #Needs tree as a variable to maintain it on the call stack in recursion
        print("--------------------------Evaluating the expression using the AST-------------------------------")
        return self.evaluatemathExprTree(tree)
        
    #recursion and use a stack
    """Post order traversal - a version of depth first search using  a stack to maintain the value to evaluate"""
    def evaluatemathExprTree(self, tree):
        #not going deeper than the leaf node
        if tree is not None:
            print("tree opvalue---", tree.opvalue)
        else:
            print("tree opvalue---", None)
        if tree is not None:
            self.evaluatemathExprTree(tree.left)
            self.evaluatemathExprTree(tree.right)
            if(tree.opvalue == '+'):
                op1 = self.evalstack.pop()
                op2 = self.evalstack.pop()
                self.evalstack.append(float(op1) + float(op2))
                #Call stack will be the same inspite of push and pop to evalstack since the calls depth has not changed
                self.printcallstack()
                self.printevalstack()
            elif(tree.opvalue == '-'):
                op1 = self.evalstack.pop()
                op2 = self.evalstack.pop()
                #Bug: int typecasting uses 0.8 as 0
                self.evalstack.append(float(op1) - float(op2))
                self.printcallstack()
                self.printevalstack()
            elif(tree.opvalue == '*'):
                op1 = self.evalstack.pop()
                op2 = self.evalstack.pop()
                self.evalstack.append(float(op1) * float(op2))
                self.printcallstack()
                self.printevalstack()
            elif(tree.opvalue == '/'):
                op1 = self.evalstack.pop()
                op2 = self.evalstack.pop()
                #popped one is the last operator :BUG
                self.evalstack.append(float(op2) / float(op1))
                self.printcallstack()
                self.printevalstack()
            else:
                self.evalstack.append(float(tree.opvalue))
                self.printcallstack()
                self.printevalstack()
            #return the top of the stack
            return(self.evalstack[-1])

    def printcallstack(self):
        print("--------------------------Call stack----------------------------")
        for line in traceback.format_stack():
            print(line.strip())
        print("--------------------------Call stack----------------------------")
    def printevalstack(self):
        print("--------------------------Eval stack----------------------------")
        i = len(self.evalstack)-1
        stackstr = ""
        while(i >= 0):
            stackstr = stackstr + " ||" + str(self.evalstack[i])
            i=i-1
        print(stackstr)
        print("--------------------------Eval stack----------------------------")
