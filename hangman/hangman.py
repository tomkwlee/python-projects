import random
from words import words
import string

def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()
    
def hangman():
    word = getValidWord(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    
    lives = 10
    
    while len(wordLetters) > 0 and lives > 0:
        print('You have', lives, 'lives and have used these letters:', ' '.join(usedLetters))
    
        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print('Current word: ', ' '.join(wordList))
        
        userLetter = input('Guess a letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                
            else:
                lives = lives - 1
                print('\nYour letter,', userLetter, 'is not in the word.')
                
                  
        elif userLetter in usedLetters:
            print('You have already used that character. please try again.')
            
        else:
            print('Invalid character. Please try again.')
            
    if lives ==0:
        print('You died. sorry, the word was', word)
    else:
        print(word,"yay! you've successfully guessed the word!")
        
hangman()