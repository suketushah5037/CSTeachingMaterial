"""This game is an implementation of a hangman game on the console. The game
randomly selects a movie name from the movielist, creates as many dashes and gives
clues for the vowels. Post that the user can guess max 7 times or guess the movie
whichever is earlier"""

#Movie list
movielist = [ 'aa', 'aba', 'abac', 'drfe']

#Select a movie
import random
#range of one less than the last item - 0 to 3
movieitem =  random.randint(0, len(movielist)-1)
#the movie selected
selectedmovie = movielist[movieitem]

#User message
print("Are you ready for a game of hangman?")

#maintain dashes as a list, since strings are immutable
#subroutine to create as many dashes as the selected movie name and return a list
def make_dashes():
    list_dashes = []
    for i in range(0, len(selectedmovie)):
        list_dashes.append("_  ")
    return list_dashes
    
#list of dashes
list_dashes = make_dashes()
#replace the vowels
vowels = ['a', 'e', 'i', 'o', 'u']

print("selected movie = ", selectedmovie)
print("dashes string", list_dashes)

#Nested loop to replace the vowels in the list of dashes
for i in range(0, len(selectedmovie)):
    for vowel in vowels:
        if(vowel == selectedmovie[i]):
            #put in a vowel and two spaces for beauty
            list_dashes[i] = vowel + '  '
print("new list of dashes = ", list_dashes)


#subroutine to decide if the movie has been guessed
def check_movieguessed(list_dashes):
    if('_  ' not in list_dashes):
        return True
    else: return False
    return(list_dashes)

#subroutine to make the list into a single string
def convert_listtostring(list_dashes):
    dashes = ""
    dashes  = dashes.join(list_dashes)
    return dashes

#convert list to string to display to the user
dashes = convert_listtostring(list_dashes)
print("Now guess this movie")
print(dashes)

#constant to maintain max guesses
MAXGUESSES = 7

#check if the movie has only vowels and nothing else, then quit, else continue
if(check_movieguessed(list_dashes)):
    print("movie name has no more letters to be guessed. Game Over")
else:
    print("Start guessing")
    # max guesses  = 7
    numberofguesses = MAXGUESSES

    #Till the movie has been guessed or the number of guesses have not got exhausted, let the user keep guessing
    while( (numberofguesses > 0) or (not(check_movieguessed))):
        guessedletter = input("Guess a letter: ")
        guessedletter = guessedletter
        print("Guessed letter = ", guessedletter)
        #find if the letter is there in the moviename
        found_index = selectedmovie.find(guessedletter)
        print("found index = ", found_index)
        if(found_index != -1):
            print("found the guessed letter")
            #replace the found letter into the list of dashes, convert it into a string and display
            #also check if game is over
            list_dashes[found_index] = guessedletter + '  '
            dashes = convert_listtostring(list_dashes)
            print(dashes)
            if(check_movieguessed(list_dashes)):
                #print("game over, you guessed all letters and won")
                break
        else:
            #reduce guesses if letter not found
            numberofguesses = numberofguesses - 1
            print("Started hanging {} turns left".format(numberofguesses))
    #when out of the loop, if no guesses left game is over
    #movie has been guessed and you won        
    if(numberofguesses == 0):
        print("Game over! you lost")
    else:
        print("all correctly guessed! you won")
