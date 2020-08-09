# This is a guess the number game
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 19')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess. ')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + 'guesses .')

print('You took' + str(guessesTaken) + ' guesses .')