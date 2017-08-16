#16C3 = 16*15*14/3*2*1

#16 * 15 * 14 = choose 3 items from 16
#4 balls RBGY choose 3 - no repetition
# RB RG RY RR
# BR BG BY BB
# GR GB GY GG
# YR YB YG YY

# RRB BRB GRB YRB
# RRG BRG GRG YRG
# RRY BRY GRY YRY
# RRR BRR GRR YRR

#total 64

#permutations with repetitions = 4*4*4 = 64

#Permutations without repetitions = 4*3*2*1/1 = RBG RBY RGB RGY RYB RYG
#6 with R in the first place, G - 6, Y - 6 B -6 = 6*4 = 24
#GRB

#Combinations - without repetition as in lottery ticket or pascals
#order is important - 24
#24/6  = 4

#Mehtod 1
#RGB RGY RBY GBY - combinations without repetitions
#nC3 = n!/(n-r)! * r!
import math

x = math.factorial(4)
#print(x)

#Method 2 - pattern recognition
pascals = []
oldlist = []
i = 1
while(i<=5):
    mylist = [None]*i
    mylist[0]=1
    j = 1
    print(i)
    if(i > 2):
        while(j < i-1): 
            #print(oldlist)
            mylist[j] = oldlist[j-1] + oldlist[j]
            j= j + 1
    mylist[i-1] = 1
    pascals.append(mylist)
    print(mylist)
    oldlist = mylist
    i = i + 1
    #print(i)

print("Pascal's triangle")
print(pascals)

##############################################################################

#With recursion
import sys
def rowitempascal(i, j):
        #print((i,j))
        if(j == 0):
            return(1)
        elif(j == (i-1)):
            return(1)
        else:
           return(rowitempascal(i-1, j-1) + rowitempascal(i-1, j))



i = 1
print("pascals with recursion")
while(i <= 5):
       
        
        j = 0
        while(j <= i - 1):
            #so that it does not ome by default with a \n
            sys.stdout.write(str(rowitempascal(i, j)) + ' ')
            j = j + 1
        print("\n")
        i = i + 1
                

##############################################################################

#Dynamic programming -
#memoization and tabulation
#Examples - Give other examples

#Pascals with memoization - store the value
#tabulation- store and build from bottom up


import sys
def rowitempascal(i, j):
        #print((i,j))
        
        if(j == 0):
            pascals[i][j] = 1
            return(1)
        elif(j == (i-1)):
            pascals[i][j] = 1
            return(1)
        elif(pascals[i][j] != -1):
            return pascals[i][j]
        else:
            pascals[i][j] = rowitempascal(i-1, j-1) + rowitempascal(i-1, j)
            return(pascals[i][j])



i = 1
print("pascals with memoization")
#For storing
pascals = [None]
while(i <= 5):
        #For storing
        mylist = [-1]*i
        pascals.append(mylist)
        
        j = 0
        while(j <= i - 1):
            #so that it does not ome by default with a \n
            #sys.stdout.write(str(rowitempascal(i, j)) + ' ')
            rowitempascal(i, j)
            j = j + 1
        #print("\n")
        i = i + 1
                
print(pascals)

##############################################################################

#Tabulation - build from bottom up

i = 1
print("pascals with tabulation ")
#For storing
pascals = [None]
while(i <= 5):
        #For storing
        mylist = [-1]*i
        pascals.append(mylist)
        j = 0
        while(j <= i - 1):
            #so that it does not ome by default with a \n
            if(j == 0):
                pascals[i][j] = 1
            if(j == (i-1)):
                pascals[i][j] = 1
            else:
                pascals[i][j] = pascals[i-1][j-1] + pascals[i-1][j]
            j = j + 1
        #print("\n")
        i = i + 1
print(pascals)

##############################################################################
#Exercise
#Try fibonacci series for the pattern based approcah, recursion, memoization and tabulation
#Other classic dynamic programming exercises
