#ax+by=c
#3x+5y=4

#leftjarfull = 5
leftjarfull = 3

#rightjarfull = 3
rightjarfull = 5


leftjar = leftjarfull
rightjar = 0

print(leftjar,rightjar)
while( (leftjar != 4) and (rightjar != 4) ):
    #take the case of (2,0)
    temp = min(leftjar, (rightjarfull - rightjar))
    #temp = rightjarfull - rightjar #temp = 3
    leftjar = leftjar - temp #leftjar =  2-3 = -1
    rightjar =  rightjar + temp #rightjar=3

    print(leftjar,rightjar)
    
    if( (leftjar == 4) or (rightjar == 4)):
        print("Solution")
        break
    
    if(leftjar == 0):
        leftjar = leftjarfull
    if(rightjar == rightjarfull):
        rightjar = 0
#ax+by=c
#a=5, b=3
##5 0
##2 0
##5 2
#5*2-3*2=4
##Solution


#ax+by=c
#a=3, b=5
##3 0
##0 3
##1 5
##0 1
##0 4
##Solution
#3*2-5*1=1
#3*2*4-5*4*4=4

#8,-16
#x=5k + 2, y=-3k-1
#x=7,y=-4

##3x+5y=4
##x=u+5w
##y=v-3w
##
##3x+5y=1
##-3*3+5*2=1
##u,v = -3,2
##
##3 * -12 + 5 * 8 = 4
##
##one solution = -12,8
##x=-12+5=-7
##y=8-3=5
##
##-21+25 = 4

#optimal
        3x+10y=8
3x+10y =1

x= 18
y=-10
        18-10=8
u=6,v=-1
