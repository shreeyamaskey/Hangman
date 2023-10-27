'''
Hangman.py
@author: Shreeya Maskey
'''

import sys
import random

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print(c,end="")
        print()

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        #print word
        self.wordguess = ['_'] * len(word)

        guesses = 0

        incorrect_guesses = [] # temporary list to keep all the guesses in
        
        while guesses < 10:
            print(' '.join(self.wordguess))
            ch = input('Enter a guess:').lower()

            #only allowing alphabetic character
            if ch.isalpha():
                #check if the input is more than one character
                #check the length of ch - it needs to be one
                chLen = lambda x: True if len(x) == 1 else False
                if chLen(ch):
                    #to print if the input has already been entered before
                    if ch in self.wordguess:
                        print("You have already entered this guess. Try again!")
                        continue
                    if ch in incorrect_guesses:
                        print("The letter", ch, "has already been used. Try again!")
                        continue
                    #check if the character is in the list words
                    i = 0
                    counter = 0 # counter to check for win

                    #mapping: x is word and y is self.wordguess. we change the y to ch if x == ch, else it remains as y
                    self.wordguess = list(map(lambda x, y: ch if x == ch else y, word, self.wordguess))

                    for i in range(len(word)):
                        if '_' in self.wordguess[i]:
                            counter += 1
                        i = i+1
                    guesses += 1

                    if counter == 0:
                        print("Congratulations! You guessed the word.")
                        print("Your guess:", ''.join(self.wordguess))
                        print("The word:", word)
                        break

                    # if counter is more than guesses left, user has lost
                    #put ch in the temp list
                    if ch not in word:
                        incorrect_guesses.append(ch)
                        print(ch, "does not occur.")
                    print("Guesses left: ", 10 - guesses)

                else:
                    print("Only one character is allowed in each input. Try again!")
                    continue
            else:
                print("Please only input alphabetic characters. Try again!")
                continue
        if guesses == 10:
            print("Sorry you are out of guesses. The word is", word)


if __name__ == "__main__":

    game = Hangman()

    game.playgame()
