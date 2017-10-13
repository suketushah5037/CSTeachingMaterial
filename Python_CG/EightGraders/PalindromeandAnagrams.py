#Palindrome

#a string
moviename = "madam"

#slicing
reversedname = moviename[::-1]
#use reverse and use join to make it a string again
#reversed2name = "".join(reverse(moviename))

#cheeck lower case for both, or store the lower cases
print(moviename.lower())
print(reversedname.lower())

#check if both the strings are the same
if(moviename.lower() == reversedname.lower()):
    print("A palindrome")
else:
    print("not a palindrome")

#anagrams

#Method 1 - check each letter with all the letters
# heart and earth

anagramstring = "heart"
secondstring = "earth"


#n times for outer loop
#inner loop can be one time if found in the first position, 2 times if second and n times if nth, n(n+1)/2 So inner and so O(n^2)
secondstringlist = list(secondstring)
for charbase in anagramstring:
    #the position of the letter found in the second string, reset it when pos of the
    #the second string is over
    secondstringpos = 0
    for charsecond in secondstring:
        if(charbase == charsecond):
            secondstringlist[secondstringpos] = None
        else:
            #increase the position
            secondstringpos = secondstringpos + 1

#All the letters have been replaced to None and hence it is an anagram
#or loop through each explicitly
if all(char is None for char in secondstringlist):
    print(anagramstring + " and " + secondstring + " are anagrams.")

#print(secondstringlist)


#Method 2 - Sort both lists alphabetically and compare
#O(nlogn) or O(n^2) based on what sorting uses
anagramstring = "heart"
secondstring = "earth"

#Convert them to lists to sort
listanagramstring = list(anagramstring)
listsecondstring = list(secondstring)

#in place sort of the strings
listanagramstring.sort()
listsecondstring.sort()

anagram = True
#position in the first string
pos = 0
print(listanagramstring)
print(listsecondstring)
 
for char1 in listanagramstring:
    if(char1 != listsecondstring[pos]):
        anagram = False
        break
    else:
        pos = pos + 1
if(anagram == True):
    print("Method 2: sorting method: anagrams")
else:
    print("Method 2: sorting method: not anagrams")


#Method 3 - Maintain the frequency of the characters
#26 letters box for the frequency of all the letters
#O(n) = only one loop
freqanagramstring = [0]* 26
freqsecondstring = [0] * 26

anagramstring = "heart"
secondstring = "earth"

#prints 7 - 8th position
#print(ord("h")-ord("a"))

#the position of the char in the frequency list
position = 0 
for eachchar in anagramstring:
    position = ord(eachchar)-ord("a")
    #increase the frequency at that position
    freqanagramstring[position] = freqanagramstring[position] + 1
    
print("Frequency table for the first string")
print(freqanagramstring)

#Do the same for the second string

#the position of the char in the frequency list
position = 0 
for eachchar in secondstring:
    position = ord(eachchar)-ord("a")
    #increase the frequency at that position
    freqsecondstring[position] = freqsecondstring[position] + 1
    
print("Frequency table for the first string")
print(freqsecondstring)


#Now compare the frequencies
position = 0
while(position < 26):
    if(freqsecondstring[position] != freqanagramstring[position]):
        print("not an anagram")
        break
    else:
        position = position + 1

print("Strings are anagrams by comparing frequencies")


#Method 4: List all anagrams of first string

#recurse through all permutations

def stringpermutations(anagramstring, leftindex, rightindex):
    if(leftindex == rightindex):
        print( "".join(anagramstring))
        if("".join(anagramstring) == secondstring):
            print("!!!!!anagrams!!!!!!")
    else:
        for i in range(leftindex,rightindex+1):
            #swap
            anagramstring[leftindex], anagramstring[i] = anagramstring[i], anagramstring[leftindex]
            print(anagramstring[leftindex] + ", " + anagramstring[i])
            print("stringpermutations(" + "".join(anagramstring) + ", " + str(leftindex+1) + ", " + str(rightindex) + ")")
            stringpermutations(anagramstring, leftindex+1, rightindex)
            print("backtrack " + anagramstring[leftindex] + ", " + anagramstring[i])
            anagramstring[leftindex], anagramstring[i] = anagramstring[i], anagramstring[leftindex] # backtrack


secondstring = "act"
# Driver program to test the above function
anagramstring = "cat"
anagramstringlen = len(anagramstring)
listanagramstring = list(anagramstring)
stringpermutations(listanagramstring, 0, anagramstringlen-1)
 
