import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)

chosen_word = random.choice(word_list)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for i in chosen_word:
    display.append("_")

while lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")    

    position = 0
    for letter in chosen_word:
        if letter == guess:
            display[position] = guess
        position += 1

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")        
    
    if "_" not in display:
        print("You win!")
        break

    if lives == 0:
        print("You lost...")
        break

    print(display)
    print(stages[lives])

print(f"{' '.join(display)}")

