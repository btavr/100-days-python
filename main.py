#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

for i in chosen_word:
    display.append("_")

while "_" in display:
    guess = input("Guess a letter: ").lower()

    position = 0
    for letter in chosen_word:
        if letter == guess:
            display[position] = guess
        position += 1

    print(display)

print("You won!")
