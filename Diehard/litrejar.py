#Referred to geekforgeeks site. Thanks to Madhur Modi
#3,6,9
#3,6,8
#2,5,1

#Diophantine equations are equations where only integral solutions are required

#linear diophantine equation - same way where there are integral values

#it has a property - gcd(a,b) is divisible by c
#ax+by =  c

#gcd(a,b) should be divisible by c

#Given two integers aa and bb:

#the Euclidean Algorithm computes GCD(a,b)
#the Extended Euclidean Algorithm gives out 2 integers xx and yy such that ax+by=GCD(a,b); mainly used when GCD(a,b)=1
#GCD is one they are coprime

#Use extended euclid's method for solving gcd

#Use it to check c % GCD(a,b) == 0

#Die hard problem - 3 litre and a 5 litre jar and retieve 5 litre jar

#using code
#5, 3, 4
#5, 0
#5-3=2, 0+3     temp = 5, 3-0 = 3
#2,0
#0,2                temp = 2, 3-0 = 2
#5, 2
#4, 3                temp = 5, 3-2 = 1

#intuition
#0, 0
#5,0
#2,3
#2,0
#0,2
#5,2
#4,3


def gcd(a,b):
    if(a == 0):
        return b
    return gcd(b%a, a)

def isPossible(a,b,c):
    #print(a, b, c)
    greatestdivisor = gcd(a,b)
    print("gcd=",greatestdivisor)
    if( (c % greatestdivisor) == 0):
        #print("divisible")
        return True
    else:
        #print("not divisible")
        return False

def swap(a,b):
    temp = b
    b = a
    a = temp
    
#3,6,9
#3,6,8
#2,5,1

def pour(fromContainer,toContainer,required):
    print(fromContainer,toContainer,required)
    #Fill the from container
    fromtemp =  fromContainer
    totemp = 0
    print(fromtemp, totemp)
    #Do till required quantity of 4 is not arrived
    while( (fromtemp != required) and (totemp != required)):
        #Add or subtract the
        #minimum of the liquid in fromtemp and totemp-toContainer
        temp = min(fromtemp, toContainer - totemp)
        #print(temp)
        fromtemp = fromtemp - temp
        totemp =  temp + totemp
        print(fromtemp, totemp)
        #If either has reacher the required - stop
        if((fromtemp == required) or (totemp == required)):
            print("Success")
            break
        #If the from container is empty fill it up
        if(fromtemp == 0):
            fromtemp = fromContainer
        #If the to container is full, empty it
        if(totemp == toContainer):
            totemp = 0
        print(fromtemp, totemp)
        
a = 3
b = 5
c = 4

#a = 18
#b = 9
#c = 2

#print("calculating feasibility")
possible = False
possible = isPossible(a,b,c)
#print(possible)
if(possible == False):
    print("not possible to solve the puzzle")
else:
    #maintain the lesser liquid in a
    if(a>b):
        swap(a,b)
        print("swapping")
    if(c > b):
        print("Wrong scenario, output is greater than the input")
    else:
        print("required = ", c)
        print("from", "to")
        pour(a,b,c)
    



