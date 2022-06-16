import random
from syslog import LOG_NEWS

def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0
    
    while guess != randomNumber:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess < randomNumber:
            print('sorry! guess again, too low')
        elif guess > randomNumber:
            print('sorry! guess again, too high')
    
    print(f'Yay! you have guess the number! {randomNumber}')

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        if low != high: 
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (h), too low (l), or correct (c)?: ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'yay! the computer guessed your number {guess}, correctly!')
    
computerGuess(500)