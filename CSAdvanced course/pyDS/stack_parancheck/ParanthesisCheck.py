#The file name Stack.py is a library which can be imported and the
#features provided by the library can be used here
import Stack

"""
Check if the math expression is balanced or not
"""
def checkBalanced(mathExpression):
    paranthesisStack =  Stack.Stack()

    #Loop through the math expression to check if balanced or not
    #What if user directly enters a closing ')'
    for char in mathExpression:
        #Brackets have been opened push on to the stack
        if(char == '('):
            paranthesisStack.push(char)
        elif(char == ')'):
            #Could use the below variables in a test case and refactor
            #What if the stack is empty here to peek?
            if(paranthesisStack.size() != 0):
                lastchar = paranthesisStack.peek()
                #If conditions to prevent popping unless it is open and close together
                if(lastchar == '('):
                    lastchar = paranthesisStack.pop()
                else:
                    #Pushing close bracket to maintain consistency of True and False and so that I do not
                    #use an extra flag
                    paranthesisStack.push(char)
                    break
            #Stack is empty
            else:
                #Pushing close bracket to maintain consistency of True and False and so that I do not
                #use an extra flag
                paranthesisStack.push(char)
                break
        else:
            #Some integer ideally or character (error - but we are not checking for the same here)
            #print("Skipping, the current character = {}", char )
            continue

    if(paranthesisStack.size() > 0):
        #there are brackets that have not been closed left in the stack
        return False
    else:
        return True


#If not loaded from a module, the __name__ variable is set to "__main__", else
#it is set to the module's name

#this if condition is written when you dont want this parantheses check code to run
#when imported as a module but only when it is the main driver
if __name__ == "__main__":
    mathExpression = input("Enter a mathematical expression with paranthesis: We shall tell you if your paranthesis is balanced or not:\n")    
    if(checkBalanced(mathExpression)):
        print("Expression is balanced")
    else:
        print("It is not balanced")
