import random
import sys

# Set up the Hangman pictures
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

# Word category
CATEGORY = 'Animals'

WORDS = """
ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM
COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK
EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD
LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL
PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN
RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE
SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE
WEASEL WHALE WOLF WOMBAT ZEBRA
""".split()


def main():
    print('Hangman Game')

    missedLetters = []
    correctLetters = []

    secretWord = random.choice(WORDS)

    while True:
        drawHangman(missedLetters, correctLetters, secretWord)

        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters.append(guess)

            foundAllLetters = True

            for letter in secretWord:
                if letter not in correctLetters:
                    foundAllLetters = False
                    break

            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break

        else:
            missedLetters.append(guess)

            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The word was:', secretWord)
                break


def drawHangman(missedLetters, correctLetters, secretWord):

    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print()

    print('Missed letters: ', end='')

    for letter in missedLetters:
        print(letter, end=' ')

    if len(missedLetters) == 0:
        print('No missed letters yet.')

    print()

    blanks = ['_'] * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    print(' '.join(blanks))


def getPlayerGuess(alreadyGuessed):

    while True:
        print('Guess a letter.')
        guess = input('> ').upper()

        if len(guess) != 1:
            print('Please enter a single letter.')

        elif guess in alreadyGuessed:
            print('You have already guessed that letter.')

        elif not guess.isalpha():
            print('Please enter a LETTER.')

        else:
            return guess


# Start the game
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()