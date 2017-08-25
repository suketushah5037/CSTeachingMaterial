
# Fibonacci series 0 1 1 2 3 5 8 13
fib = 0
#Hardcoding the first two numbers as 0 and 1 in oldoldfib and oldfib respectively
oldfib = 1
oldoldfib = 0

#the iterator
i  = 0

#Number of items in the series
NOOFFIBITEMS  = 10

#Heading for the table
print("fib", "oldfib", "oldoldfib")

#Loop to print the series
while(i < NOOFFIBITEMS):
    print(fib, '\t', oldfib, '\t', oldoldfib)
    #The first item in the series is erased and stores the second item in it
    oldoldfib = oldfib
    #The second item stored the fib number calculated before(in the first case it is 0)
    oldfib = fib
    #calculating the fib as sum of previous two items in the series
    fib = oldoldfib + oldfib
    i = i + 1

#Take an easier example
#To understand the stack trace usng prints

#Take an example of factorial
#n*fact(n-1)

def fact(n):
    if(n == 1):
        return 1
    else:
        print(str(n) + "*" + "fact(" + str(n-1) + ")")
        return n*fact(n-1)
i = 1
while(i <= 5):
    print("Factorial of " + str(i))
    print(fact(i))
    i = i + 1


#Recursive method
#All the variables in the function go in the stack
#The fib(n-1) and fib(n-2) also go into the stack
#The stack unwinds and calculates the values
def fib(n):
    if(n <= 1):
        return n
    else:
        #print("fib(" + str(n-1) + ")" + "+" + "fib(" + str(n-2) + ")" )
        return fib(n-1) + fib(n-2)

print("fibonacci series - recursion")
iter = NOOFFIBITEMS
#biggest to smallest
while(iter >= 0):
    print(fib(iter))
    iter = iter - 1
#smallest to bigeest
print("fibonacci series - recursion - small to big")
iter = 0
while(iter <= NOOFFIBITEMS):
    print(fib(iter))
    iter = iter + 1



#Memoization

#The stack unwinds and calculates the values
#If present in the cache - do not calculate
def fib(n):
    if(fiblist[n] != -1):
        return fiblist[n]
    elif(n <= 1):
        fiblist[n] = n
        return n
    else:
        #print("fib(" + str(n-1) + ")" + "+" + "fib(" + str(n-2) + ")" )
        fiblist[n] = fib(n-1) + fib(n-2)
        return fiblist[n]


print("fibonacci series - memoization")
iter = 0
#Create a cache
fiblist = [-1] * NOOFFIBITEMS
#smallest to bigeest
iter = 0
while(iter < NOOFFIBITEMS):
    print(fib(iter))
    iter = iter + 1

#Tabulation
#Calculate from bottom up

#No recursion here
print("with tabulation")

iter = 0
#Create a cache
fiblist = [-1] * NOOFFIBITEMS
while(iter < NOOFFIBITEMS):
    if(iter <= 1):
        fiblist[iter] = iter
    else:
        fiblist[iter] = fiblist[iter-1] + fiblist[iter-2]
    iter = iter + 1

print(fiblist)
