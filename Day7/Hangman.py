#https://hangmanwordgame.com/?fca=1&success=0#/
#https://en.wikipedia.org/wiki/Hangman_(game)

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")    
