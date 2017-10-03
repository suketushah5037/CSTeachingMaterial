#Movie list

movielist = [ 'aa', 'aba', 'abac', 'drfe']

#Select a movie

import random

#range of one less than the last item - 0 to 3
movieitem =  random.randint(0, len(movielist)-1)

selectedmovie = movielist[movieitem]

print("Are you ready for a game of hangman?")

def make_dashes():
    list_dashes = []
    for i in range(0, len(selectedmovie)):
        list_dashes.append("_  ")
    return list_dashes

list_dashes = make_dashes()
#replace the vowels
vowels = ['a', 'e', 'i', 'o', 'u']

print("selected movie = ", selectedmovie)
print("dashes string", list_dashes)

for i in range(0, len(selectedmovie)):
    for vowel in vowels:
        if(vowel == selectedmovie[i]):
            #put in a vowel and two spaces for beauty
            list_dashes[i] = vowel + '  '
print("new list of dashes = ", list_dashes)


def check_movieguessed(list_dashes):
    if('_  ' not in list_dashes):
        return True
    else: return False
        
    return(list_dashes)
def convert_listtostring(list_dashes):
    dashes = ""
    dashes  = dashes.join(list_dashes)
    return dashes

dashes = convert_listtostring(list_dashes)
print("Now guess this movie")
print(dashes)

if(check_movieguessed(list_dashes)):
    print("movie name has no more letters to be guessed. Game Over")
else:
    print("Start guessing")

    numberofguesses = 7
    while( (numberofguesses > 0) or (not(check_movieguessed))):
        guessedletter = input("Guess a letter: ")
        guessedletter = guessedletter
        print("Guessed letter = ", guessedletter)
        #foung the letter
        found_index = selectedmovie.find(guessedletter)
        print("found index = ", found_index)
        if(found_index != -1):
            print("found the guessed letter")
            list_dashes[found_index] = guessedletter + '  '
            dashes = convert_listtostring(list_dashes)
            print(dashes)
            if(check_movieguessed(list_dashes)):
                #print("game over, you guessed all letters and won")
                break
        else:
            numberofguesses = numberofguesses - 1
            print("Started hanging {} turns left".format(numberofguesses))

    if(numberofguesses == 0):
        print("Game over! you lost")
    else:
        print("all correctly guessed! you won")
