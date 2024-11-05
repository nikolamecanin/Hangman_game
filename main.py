import random

from hangman_art import logo,stages
from hangman_words import word_list
print(logo)
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for i in range(word_length):
    placeholder+="_"
print(placeholder)
corrected_answers = []

game_over = False
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess the word: ").lower()

    if guess in corrected_answers:
        print(f"You've already tried with letter {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display+=guess
            corrected_answers.append(guess)
        elif letter in corrected_answers:
            display+=letter
        else:
            display+="_"

    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            print(f"Game over. It was a word {chosen_word}")
            game_over = True

    if "_" not in display:
        print("You win!")
        game_over = True

    print(display)
    print(stages[lives])
