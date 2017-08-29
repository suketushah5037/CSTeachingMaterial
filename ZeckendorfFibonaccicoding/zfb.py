# Python program for Zeckendorf's theorem. It finds representation
# of n as sum of non-neighbouring Fibonacci Numbers.

# Returns the greatest Fibonacci Numberr smaller than
# or equal to n.
def nearestSmallerEqFib(n):
	
	# Corner cases
	if (n == 0 or n == 1):
		return n
		
	# Finds the greatest Fibonacci Number smaller
	# than n.
	f1,f2,f3 = 0,1,1
	#print("f1", "f2", "f3")
	#print(f1, f2, f3)
	#till the last number does not go above the number required to be split
	#for 24 - 21 in the first case and 3 in the next case
	while (f3 <= n):
		f1 = f2;
		f2 = f3;
		f3 = f1+f2;
		#print(f1, f2, f3)
	#returns 21 the first time and 3 the next
	return f2;


# Prints Fibonacci Representation of n using
# greedy algorithm
def printFibRepresntation(n):
	
	while (n>0):

		# Find the greates Fibonacci Number smaller
		# than or equal to n
		f = nearestSmallerEqFib(n);

		# Print the found fibonacci number
		print(f)

		# Reduce n, 24-21 = 3, send 3 for split
		n = n-f

# Driver code test above functions
n =24
print("Non-neighbouring Fibonacci Representation of", n, "is")
printFibRepresntation(n)
