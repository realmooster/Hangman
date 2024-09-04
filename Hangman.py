guess = [
    'pineapple',
    'strikebreaker',
    'revolution',
    'payment',
    'regard',
    'impress',
    'king',
    'queen',
    'empress',
    'water',
]

print("~~~~~~~~~~~~~~~~ Welcome To Hangman ~~~~~~~~~~~~~~~~")

#Group of Words above for user to choose to guess.
ask_user = int(input('Choose a number between for a word: 0-9: '))
split_word = guess[ask_user]
displaything = len(split_word)
turns = 12
wrong = "~~~~~~ WRONG ~~~~~~:"
correct = []

#Breaks each individual character into a list from the word and the underscores/PlaceHolders
def display():
    global broken_word
    global split_underscore
    underthing = "_" * displaything
    #Broken_word allows the word that was selected to be broken up into characters to choose an index
    broken_word = list(split_word)
    #To replace each index with the appropriate letter
    split_underscore = list(underthing)
    print(split_underscore)
display()

def connect():
    global turns
    global pick
    global location
    global repeat
    global wrong
    while turns > 0: 
        pick = input("Pick a letter: ")
        #Checks if the letter is already in the list of wrong letters
        if pick in wrong:
            print("You have already guess this letter.")
            print(wrong)
        #If the letter is not in the wrong letter list, it adds it on to it and removes a turn for getting it wrong
        elif pick not in broken_word:
            wrong += " " + pick
            print(wrong)
            print("That letter is not in this word.")
            turns -= 1
            print("You have " + str(turns) + " guesses left.")
        #Checks if the letter is already in the list of right letters
        elif pick in correct:
            print("You have already guessed this letter.")
        #If the letter is not in the list of right letters, it adds the letter to the list. 
        elif pick not in correct:
            correct.append(pick)
            print("That letter is in this word.")

            location = broken_word.index(pick)
            split_underscore[location] = broken_word[location]
            print(split_underscore)

            if "_" not in split_underscore:
                print("You won.")
                break


connect()

if turns <= 0:
    print("You lose. The word was: ---------------> " + split_word)