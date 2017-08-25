#Recursive fibonacci

#Recursive method
#All the variables in the function go in the stack
#The fib(n-1) and fib(n-2) also go into the stack
#The stack unwinds and calculates the values
def fib(n):
    if(n <= 1):
        return n
    else:
        return fib(n-1) + fib(n-2)

    
#print("fibonacci series - recursion")

def test():
    iter = 0
    while(iter <= 10):
        iter = iter + 1

