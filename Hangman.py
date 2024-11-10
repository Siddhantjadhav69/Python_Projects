#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

Word = random.choice(word_list)

display = []
for letter in Word:
    display += "_"
print(display)

guess = input("Guess a Letter : ").lower()

for Position in range(len(Word)):
    letter = Word[Position]
    if letter == guess :
        print("Right")
    else:
        print("Wrong")
print(display)