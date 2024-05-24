import random

#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for i in chosen_word:
    display.append("_")

while lives > 0:
    guess = input("Guess a letter: ").lower()

    position = 0
    for letter in chosen_word:
        if letter == guess:
            display[position] = guess
        position += 1

    if guess not in chosen_word:
        lives -= 1
    
    if "_" not in display:
        print("You win!")
        break

    if lives == 0:
        print("You lost...")
        break

    print(display)
    print(stages[lives])

print(f"{' '.join(display)}")

